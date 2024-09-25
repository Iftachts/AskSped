import streamlit as st
import google.generativeai as genai
import os
from pyairtable import Api

st.markdown("""
<style>
    body {
        direction: rtl;
    }
    .stApp {
        direction: rtl;
    }
    .stTextArea textarea {
        direction: rtl;
    }
    .stMarkdown {
        text-align: right;
    }
    .stButton {
        text-align: right;
    }
    /* Apply RTL to specific elements where Hebrew is expected */
    .hebrew-text {
        direction: rtl;
        unicode-bidi: bidi-override;
        text-align: right;
    }
    /* This selector allows English content to remain LTR */
    .english-text {
        direction: ltr;
        unicode-bidi: normal;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

with open('hozerupdated.txt', 'r', encoding='utf-8') as file:
    hozer = file.read()
    
# Airtable setup
base_id = 'app8UFiZQuyxJ9zZp'
table_name = 'info'
feedback_table_name = 'feedback'  # New table for feedback
personal_access_token = os.getenv('AirtableToken')  # Use environment variable in production 
# Initialize the Airtable API and get the tables
api = Api(personal_access_token)
table = api.table(base_id, table_name)
feedback_table = api.table(base_id, feedback_table_name)

# Create a global placeholder for the message display at the top level of your script
message_display = st.empty()
api_key = os.getenv('GeminiApikey')
genai.configure(api_key=api_key)
# Set up the model and other configurations as in your provided code
# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": [hozer]
  },
  {
    "role": "model",
    "parts": ["## Analysis of the Hebrew Text\n\nThe provided Hebrew text appears to be a detailed guideline for the operation of committees responsible for assessing eligibility and determining the type and extent of special education services for students with disabilities in the Israeli education system. \n\nHere's a breakdown of the document:\n\n**1. Introduction:**\n\n*   Outlines the changes brought by Amendment 11 to the Special Education Law of 1988.\n*   Emphasizes the shift towards inclusion and providing special education services within mainstream classrooms.\n*   Highlights the importance of collaboration between different professionals and parents in the decision-making process.\n*   Defines key terms and committees involved:\n    *   **Multi-Professional Team (MPT):** determines eligibility for support within mainstream settings.\n    *   **Eligibility and Characterization Committee (ECC):** assesses eligibility for special education services and determines the level of support needed.\n    *   **Objection Committee:** reviews objections to decisions made by the ECC.\n\n**2. Multi-Professional Team (MPT):**\n\n*   Defines the composition of the MPT (principal, teacher, psychologist, special education professional).\n*   Specifies the target population for MPT assessment (students in mainstream settings who require support).\n*   Outlines the procedures for convening the MPT, including timelines, documentation, and decision-making processes.\n*   Explains the process of determining the composition of individual support packages for eligible students.\n*   Details the creation and implementation of Individual Educational Programs (IEPs) for students in mainstream settings.\n*   Explains the process of objecting to MPT decisions through the ECC.\n\n**3. Eligibility and Characterization Committee (ECC):**\n\n*   Defines the composition of the ECC (Ministry of Education representative, local education authority representative, special education inspector, general education inspector, educational psychologist, parent representative).\n*   Specifies the target population for ECC assessment (students with disabilities requiring significant support).\n*   Outlines the procedures for referring students to the ECC, including timelines, documentation, and the decision-making process.\n*   Explains the different types of educational settings and support services available, including individual support packages.\n*   Details the process of choosing the appropriate educational setting for the student based on their needs and parental preferences.\n*   Explains the process of objecting to ECC decisions through the Objection Committee.\n\n**4. Objection Committee:**\n\n*   Defines the composition of the Objection Committee (district director, district educational psychologist, special education inspector, general education inspector, parent representative, public organization representative).\n*   Specifies the procedures for submitting objections to ECC decisions.\n*   Outlines the process of reviewing objections and making final decisions.\n\n**5. Appendices:**\n\n*   Provide additional information and forms related to the committees and the assessment process. \n*   Includes information on types of support, guidelines for decision-making, and lists of recognized disabilities and psychiatric diagnoses. \n\n**Overall, this document provides a comprehensive framework for ensuring that students with disabilities in Israel receive appropriate and individualized support to succeed in their educational journey.**"]
  },
  {
    "role": "user",
    "parts": ["אתה מומחה בלהבין נהלים של משרד החינוך בעזרת הטקסט שצורף קודם לכן. אתה עונה לכל שאלה במדויק ובקיצור, ובהתבסס על המידע שבשיחה זו בלבד. אם המידע לא נמצא בטקסט, ציין כי המידע לא נמצא בחוזר מנכל זה. האם מובן?"]
  },
  {
    "role": "model",
    "parts": ["בהחלט, מובן. אשתמש בידע שצברתי מהטקסט שסופק כדי לענות על שאלותיך בנוגע לנהלי משרד החינוך, בדיוק ובקיצור. שאל/י."]
  },
])

def send_and_display_message():
    message_display = st.empty()
    user_input = st.session_state.user_message.strip()
    if user_input:
        try:
            with st.spinner('ממתין לתשובה...'):
                convo.send_message(user_input)
                response = convo.last.text
            
            if response:
                message_display.markdown(f"<div class='hebrew-text' style='border:2px solid blue; padding:10px;'>{response}</div>", unsafe_allow_html=True)
                 # Store the question and response in Airtable
                record = table.create({'Question': user_input, 'Response': response})
            else:
                message_display.markdown("**No response received, please try again.**", unsafe_allow_html=True)
        except Exception as e:
            message_display.markdown(f"**Error:** {str(e)}", unsafe_allow_html=True)
        finally:
            # Clear the input field after sending the message or receiving the response
            st.session_state.user_message = ""
    else:
        st.error("Please enter a valid message.")

def submit_feedback():
    feedback = st.session_state.feedback.strip()
    if feedback:
        try:
            feedback_table.create({'Feedback': feedback})
            st.success("תודה על המשוב שלך!")
            st.session_state.feedback = ""
        except Exception as e:
            st.error(f"Error submitting feedback: {str(e)}")
    else:
        st.error("Please enter valid feedback.")

st.title("שאלו את חוזר המנכל")
st.header("חוק יישום החינוך המיוחד")
# Set up UI for input
user_message = st.text_area(label=' ', key="user_message", placeholder='כתבו כאן את שאלתכם')
send_button = st.button("שלחו", on_click=send_and_display_message)
st.markdown("<div class='hebrew-text'>השאלה נשלחת למודל שפה (גוגל ג'מיני 1.5 פרו), אשר הוזן בחוזר המנכל, וממנו מתקבלות התשובות</div>", unsafe_allow_html=True)
st.markdown("<div class='hebrew-text'>המידע המופיע בתשובות לשאלות יכול להתאפיין באי דיוקים, מומלץ לוודא את נכונות המידע בחוזר המנכל</div>", unsafe_allow_html=True)
link = "https://apps.education.gov.il/mankal/Horaa.aspx?siduri=385"
st.markdown(f"<div class='hebrew-text'><a href='{link}'>לחץ כאן</a> לכניסה לחוזר המנכל עליו מתבססות התשובות</div>", unsafe_allow_html=True)
with st.expander("רשימת שאלות לדוגמא"):
    st.markdown(
        """
        <div class='hebrew-text'>
        |   | שאלות לדוגמא|
        |---|----------------------------------------------|
        |   | אבקש רשימה מלאה של האבחנות הפסיכיאטריות המאפשרות מתן אפיון נפשי |
        |   | יש לי תלמיד שאני מודאג לגביו, מה הם השלבים עד שיוכל לקבל עזרה נוספת? |
        |   | באילו תנאים תלמיד שקיבל אפיון של לקות למידה יכול לקבל שעות סייעת? |
        |   | מי הם חברי הצוות הרב מקצועי? |
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown("<div class='hebrew-text'>ליצירת קשר: iftachts@gmail.com</div>", unsafe_allow_html=True)

# Feedback section
st.header("משוב")
feedback = st.text_area("אנא שתפו איתנו את המשוב שלכם על האפליקציה:", key="feedback")
submit_button = st.button("שלח משוב", on_click=submit_feedback)
