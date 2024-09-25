import streamlit as st
import google.generativeai as genai
import os
from pyairtable import Api

st.markdown("""
<style>
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: Right;
}

/* Apply RTL to specific elements where Hebrew is expected */
.hebrew-text {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}

/* This selector allows English content to remain LTR */
.english-text {
    direction: LTR;
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
personal_access_token = os.getenv('AirtableToken')  # Use environment variable in production 
# Initialize the Airtable API and get the table
api = Api(personal_access_token)
table = api.table(base_id, table_name)

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
  {
    "role": "user",
    "parts": ["זהו מבנה המסמך:\n\n\n\n1. מבוא\n\n\n מבוא כללי להוראה ולתיקון לחוק חינוך מיוחד.\n\n\n2. מקצועי - הרב צוות\n\n\n 2.1 כללי\n \n  תפקיד ומטרות הצוות הרב מקצועי.\n \n 2.2 סמכויות ותפקידיו של מקצועי - הרב צוות\n \n  פירוט סמכויות הצוות, לרבות קביעת זכאות, הרכב סל תמיכה, תוכנית אישית, ועוד.\n \n 2.3 אוכלוסיית יעד\n \n  הגדרת אוכלוסיית היעד עבור דיוני הצוות הרב מקצועי.\n \n 2.4 הרכב מקצועי - הרב צוות\n \n  פירוט חברי הצוות ותפקידיהם.\n \n 2.5 המוזמנים לדיון במקצועי - הרב צוות\n \n  הגדרת המוזמנים לדיון, לרבות הורים, תלמיד, מפקח, ועוד.\n \n 2.6 מקום התכנסותו של מקצועי - הרב צוות\n \n  הנחיות לגבי מיקום הדיונים.\n \n 2.7 לוח זמנים לעבודת מקצועי - הרב צוות\n \n  לוחות זמנים להגשת בקשות, קיום דיונים, קבלת החלטות, ועוד.\n \n 2.8 מעברים בין חטיבות גיל ובין מוסדות חינוך\n \n  הנחיות לגבי דיוני הצוות הרב מקצועי במעברים בין מסגרות חינוך.\n \n 2.9 ההיערכות לדיון במקצועי - הרב צוות\n \n  הנחיות כלליות והנחיות לגבי גורמים שיכולים להפנות בקשה לדיון.\n \n 2.10 מהלך הדיון וקבלת ההחלטות במקצועי - הרב צוות\n \n  פירוט מהלך הדיון, לרבות הצגת מידע, שיתוף הורים ותלמיד, קבלת החלטות, ועוד.\n \n 2.11 פרוטוקול הדיון ומכתב ההחלטה\n \n  הנחיות לכתיבת פרוטוקול הדיון ולשליחת מכתב החלטה להורים.\n \n 2.12 קביעת הרכב התמיכות בסל האישי של התלמיד (פילוח התמיכות)\n \n  הנחיות לקביעת סוגי התמיכות ופילוחן בהתאם לצורכי התלמיד.\n \n 2.13 קביעת התוכנית האישית לתלמיד בגן ובכיתה רגיל לחינוך\n \n  הנחיות לכתיבת תוכנית אישית לתלמידים במסגרות חינוך רגיל.\n \n 2.14 השגה על החלטת מקצועי - הרב צוות במעמד ועדת ואפיון זכאות\n \n  הנחיות להגשת השגה על החלטת הצוות והדיון בהשגה.\n \n\n\n3. ועדת ואפיון זכאות\n\n\n 3.1 כללי\n \n  תפקיד ומטרות הוועדה.\n \n 3.2 הוראות כלליות\n \n  הנחיות לגבי מיקום דיונים, תוקף זכאות, תדירות דיונים, ועוד.\n \n 3.3 סמכויות הוועדה\n \n  פירוט סמכויות הוועדה, לרבות קביעת זכאות, אפיון מוגבלות, קביעת רמת תפקוד, ועוד.\n \n 3.4 אוכלוסיית יעד\n \n  הגדרת אוכלוסיית היעד עבור דיוני הוועדה.\n \n 3.5 הרכב ועדת ואפיון זכאות והמוזמנים לדיון\n \n  פירוט הרכב הוועדה, מינוי חברים, והגדרת המוזמנים לדיון.\n \n 3.6 לוח זמנים לעבודת ועדת ואפיון זכאות\n \n  לוחות זמנים להגשת בקשות, קיום דיונים, קבלת החלטות, ועוד.\n \n 3.7 מסמכים לדיון בוועדת ואפיון זכאות\n \n  הנחיות לגבי המסמכים הנדרשים לדיון בוועדה.\n \n 3.8 ההפניה אל ועדת ואפיון זכאות\n \n  הנחיות לגבי תהליך ההפניה לוועדה.\n \n 3.9 מהלכים לקראת ובסיום הדיון בוועדת ואפיון זכאות\n \n  הנחיות לגבי היערכות לדיון ותפקידים לאחר הדיון.\n \n 3.10 מהלך הדיון וקבלת ההחלטות בוועדת ואפיון זכאות\n \n  פירוט מהלך הדיון, לרבות הצגת מידע, שיתוף הורים ותלמיד, קבלת החלטות, ועוד.\n \n 3.11 קביעת התוכנית האישית לתלמיד במסגרות החינוך המיוחד\n \n  הנחיות לכתיבת תוכנית אישית לתלמידים במסגרות חינוך מיוחד.\n \n 3.12 השגה על החלטת מקצועי - הרב צוות כוועדת ביושבה ואפיון זכאות\n \n  הנחיות להגשת השגה על החלטת הצוות והדיון בהשגה.\n \n 3.13 תלמיד המעביר את מקום מגוריו מיישוב אחד ליישוב אחר\n \n  הנחיות לגבי תלמידים שמעבירים מקום מגורים.\n \n 3.14 ועדות ואפיון זכאות לתלמידים המתגוררים במוסדות פנימייתיים\n \n  הנחיות לגבי תלמידים במסגרות פנימייתיות.\n \n 3.15 ועדות ואפיון זכאות לתלמידים המתגוררים במשפחות אומנה\n \n  הנחיות לגבי תלמידים במשפחות אומנה.\n \n 3.16 תשלום לנציג ארגוני הורים המשמש חבר בוועדת ואפיון זכאות\n \n  הנחיות לתשלום לנציג ארגון הורים.\n \n\n\n4. ועדת השגה\n\n\n 4.1 כללי\n \n  תפקיד ומטרות הוועדה.\n \n 4.2 סמכויות הוועדה\n \n  פירוט סמכויות הוועדה.\n \n 4.3 הרכב ועדת השגה והמוזמנים לדיון\n \n  פירוט הרכב הוועדה, מינוי חברים, והגדרת המוזמנים לדיון.\n \n 4.4 ההפניה אל ועדת השגה\n \n  הנחיות לגבי תהליך ההפניה לוועדה.\n \n 4.5 היערכות לקראת הדיון בוועדת השגה\n \n  הנחיות לגבי היערכות לדיון.\n \n 4.6 המסמכים המשמשים את ועדת השגה בקבלת החלטות\n \n  הנחיות לגבי המסמכים הנדרשים לדיון בוועדה.\n \n 4.7 מהלך הדיון וקבלת ההחלטות בוועדת השגה\n \n  פירוט מהלך הדיון, לרבות הצגת מידע, שיתוף הורים ותלמיד, קבלת החלטות, ועוד.\n \n 4.8 תשלום לנציגי ארגוני הורים וארגון ציבורי בוועדת השגה\n \n  הנחיות לתשלום לנציג ארגון הורים וארגון ציבורי.\n \n\n\n5. נספחים\n\n\n אוסף טפסים, הצהרות, לוחות זמנים, רשימות והנחיות רלוונטיות."]
  },
  {
    "role": "model",
    "parts": ["נכון, זוהי תמצית מבנה המסמך המפרטת את הוועדות השונות הפועלות מתוקף חוק החינוך המיוחד, סמכויותיהן, הרכבן, תהליכי הדיון בהן והמסמכים הנדרשים."]
  },
  {
    "role": "user",
    "parts": ["זאת רשימת הנסםחים:\n\n\n1. נספח - לוח זמנים\nמוסדי\n\n•           לוח\nזמנים מפורט לפעילות הוועדות השונות וצוותי החינוך.\n\n2. נספח - טפסי ויתור סודיות\n\n•           2.1\nטופס ויתור סודיות - להעברת מידע לוועדת ואפיון זכאות\n\n•           2.2\nטופס ויתור סודיות - להעברת מידע לוועדת השגה\n\n•           2.3\nטופס ויתור סודיות - להעברת מידע למקצועי-הרב צוות\n\n3. נספח - טופס הצהרה על שמירת סודיות\nשל המשתתפים בוועדות מתוקף חוק חינוך מיוחד\n\n4. נספח - טפסים לדיון במקצועי - הרב\nצוות\n\n•           4.2\nשאלון הפניה לדיון במקצועי - רב צוות לתלמידים הלומדים בבית הספר\n\n•           4.3\nהזמנת התלמיד וההורים לדיון במקצועי - הרב צוות (מופק מהמערכת הממוחשבת)\n\n•           4.4\nפרוטוקול דיון מקצועי-רב צוות לקביעת זכאות לשירותי חינוך מיוחדים (מופק מהמערכת\nהממוחשבת)\n\n•           4.5\nהודעה להורים על החלטת מקצועי-הרב צוות - התלמיד זכאי לשירותי חינוך מיוחדים (מופק\nמהמערכת הממוחשבת)\n\n•           4.6\nהודעה להורים על החלטת מקצועי-הרב צוות - התלמיד אינו זכאי לשירותי חינוך מיוחדים\n(מופק מהמערכת הממוחשבת)\n\n•           4.7\nפרוטוקול דיון מקצועי-הרב צוות לקביעת הרכב סל השירותים (מופק מהמערכת הממוחשבת)\n\n5. נספח - טפסים לדיון בוועדת ואפיון\nזכאות במעמד מקצועי - הרב צוות כהשגה על החלטתו\n\n•           5.1\nהזמנת התלמיד וההורים לדיון בוועדת ואפיון זכאות כהשגה על החלטת מקצועי-הרב צוות\n\n•           5.2\nפרוטוקול דיון ועדת ואפיון זכאות ביושבה כהשגה על החלטת מקצועי-רב צוות\n\n•           5.3\nהודעה להורים על החלטת ועדת ואפיון זכאות ביושבה כהשגה על החלטת מקצועי-רב צוות -\nקבלת ההשגה\n\n•           5.4\nהודעה להורים על החלטת ועדת ואפיון זכאות ביושבה כהשגה על החלטת מקצועי-רב צוות -\nדחיית ההשגה\n\n6. נספח - טפסים לוועדת ואפיון זכאות\n\n•           6.1\nשאלון הפניה לדיון בוועדת ואפיון זכאות/ מקצועי- רב צוות לדיון לתלמידים הלומדים\nבגן\n\n•           6.2\nשאלון הפניה לדיון בוועדת ואפיון זכאות לתלמידים הלומדים בבית הספר\n\n•           6.3\nשאלון להורים לקראת דיון ואפיון זכאות (בחירה)\n\n•           6.4\nשאלון לתלמיד לקראת דיון ואפיון זכאות (בחירה)\n\n•           6.5\nטופס סיכום דיון והסכמת הורים לקיום ועדת ואפיון זכאות בנוכחות חברי הוועדה בלבד\n(למילוי על ידי צוות החינוכית המסגרת במקרים המפורטים בסעיף 3.4.4)\n\n•           6.6\nהזמנת התלמיד וההורים לדיון בוועדת ואפיון זכאות (מופק מהמערכת הממוחשבת)\n\n•           6.7\nזימון מוזמנים לדיון בוועדת ואפיון זכאות (מופק מהמערכת הממוחשבת)\n\n•           6.8\nזימון חברי הוועדה לדיון בוועדת ואפיון זכאות (מופק מהמערכת הממוחשבת)\n\n•           6.9\nפרוטוקול ועדת ואפיון זכאות בדבר זכאות והחלטה (מופק מהמערכת הממוחשבת)\n\n•           6.10\nמכתבים להורים על החלטת ואפיון זכאות\n\no          6.10.1 מכתב להורים על החלטת ועדת\nואפיון זכאות לפני בחירת ההורים בנושא סוג המסגרת\n\no          6.10.2 מכתב להורים על החלטת ועדת\nואפיון זכאות - התלמיד זכאי אישי לסל\n\no          6.10.3 מכתב להורים על החלטת ועדת\nואפיון זכאות - התלמיד זכאי ללמוד במוסד חינוך מוכר בו ניתנים שירותי חינוך\nמיוחדים או בכיתה בה ניתנים שירותי חינוך מיוחדים\n\no          6.10.4 מכתב להורים על החלטת ועדת\nואפיון זכאות - התלמיד זכאי לתמיכה ממסל המוסדי/ סל שילוב והכלה בגן או בכיתה רגיל\nלחינוך\n\no          6.10.5 מכתב להורים על החלטת ועדת\nואפיון זכאות - התלמיד אינו זכאי לשירותי חינוך מיוחדים\n\no          6.10.6 מכתב לתלמיד שהוריו אינם זכאים\nלבחור את סוג החינוכית המסגרת\n\n•           6.11\nחידוש זכאות לשירותי חינוך מיוחדים לתלמיד בהאחרונה שנת לימודיו במערכת החינוך\n\n•           6.12\nהמלצת הפסיכולוג על שינוי אפיון המוגבלות בוועדת ואפיון זכאות (למידה ללקות,\nהתפתחותי מעיכוב)\n\n7. נספח - טפסים לדיון בוועדת השגה\n\n•           7.1\nהזמנת התלמיד וההורים לדיון בוועדת השגה מחוזית\n\n•           7.2\nפרוטוקול דיון ועדת השגה בעניין השגה על החלטה של ועדת ואפיון זכאות\n\n•           7.3\nהודעה להורים על החלטת ועדת השגה - קבלת ההשגה\n\n•           7.4\nהודעה להורים על החלטת ועדת השגה - דחיית ההשגה\n\n•           7.5\nהודעה להורים על החלטת ועדת השגה - החזרה לדיון בוועדת ואפיון זכאות\n\n8. נספח - המלצת הפסיכולוג החינוכית\nהמסגרת מטעם ח\"השפ בדיון מקצועי-הרב צוות\n\n9. נספח - גורמים שאבחנתם קבילה\nבוועדות מתוקף חוק חינוך מיוחד (תוספת ראשונה לחוק חינוך מיוחד)\n\n10. נספח - (דף עזר) קווים מנחים\nבתהליך קבלת החלטה בדיון בוועדות מתוקף חוק חינוך מיוחד\n\n11. נספח - רשימת הנדירות התסמונות\nוהמחלות ורשימת האבחנות הפסיכיאטריות\n\n•           11.1\nרשימת הנדירות התסמונות והמחלות\n\n•           11.2\nרשימת האבחנות הפסיכיאטריות\n\n12. נספח - מענה בהתאם לסוג המוגבלות\nולרמת התפקוד\n\n•           12.1\nתוספת שנייה לחוק חינוך מיוחד - מענה בהתאם לסוג המוגבלות ולרמת התפקוד\n\n•           12.2\nקווים מנחים לקביעת תוספת תמיכה במידת הצורך\n\n13. נספח - טפסים לוועדת ואפיון זכאות\n- חומרת המוגבלות\n\n•           13.1\nחומרת המוגבלות לתלמידים עם פיזית מוגבלות ועם נדירות תסמונות ומחלות (59, 98)\n\n•           13.2\nחומרת המוגבלות בשמיעה\n\n•           13.3\nחומרת המוגבלות בראייה\n\n14. נספח - טופס בחירת ההורים את סוג\nהחינוכית המסגרת שבה ילמד ילדם\n\n15. נספח - מידע על סוגי תמיכה לדיון\nמקצועי-הרב צוות בהרכב סל התמיכות של התלמיד\n\n•           15.1\nמידע על הבריאות ממקצועות טיפול ואומנויות באמצעות טיפול\n\n•           15.2\nמידע על התנהגות ניתוח והתערבות בגישה ההתנהגותית-הקוגניטיבית (CBT)\n\n16. נספח - הסכמת הורים להעברת מידע\nבדואר אלקטרוני מהצוות המקצועי - הרב / ואליו / מוועדת ואפיון זכאות ואליו"]
  },
  {
    "role": "model",
    "parts": ["תודה על הפירוט המלא של רשימת הנספחים. זוהי אכן רשימה מקיפה של הטפסים, ההצהרות וההנחיות הנדרשות לצורך התנהלות תקינה של הוועדות השונות הפועלות מתוקף חוק החינוך המיוחד. \n\nהאם יש שאלות ספציפיות בנוגע לנספח מסויים או לתהליך מסויים?"]
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
                message_display.markdown(f"<div style='border:2px solid blue; padding:10px;'>{response}</div>", unsafe_allow_html=True)
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


st.title("שאלו את חוזר המנכל")
st.header("חוק יישום החינוך המיוחד")
# Set up UI for input
user_message = st.text_area(label=' ', key="user_message", placeholder='כתבו כאן את שאלתכם')
send_button = st.button("שלחו", on_click=send_and_display_message)
st.write("השאלה נשלחת למודל שפה (גוגל ג'מיני 1.5 פרו), אשר הוזן בחוזר המנכל, וממנו מתקבלות התשובות")
st.write("המידע המופיע בתשובות לשאלות יכול להתאפיין באי דיוקים, מומלץ לוודא את נכונות המידע בחוזר המנכל")
link = "https://apps.education.gov.il/mankal/Horaa.aspx?siduri=385"
st.markdown(f'[לחץ כאן]({link}) לכניסה לחוזר המנכל עליו מתבססות התשובות ')
with st.expander("רשימת שאלות לדוגמא"):
    st.markdown(
        """
        |   | שאלות לדוגמא|
        |---|----------------------------------------------|
        |   | אבקש רשימה מלאה של האבחנות הפסיכיאטריות המאפשרות מתן אפיון נפשי |
        |   | יש לי תלמיד שאני מודאג לגביו, מה הם השלבים עד שיוכל לקבל עזרה נוספת? |
        |   | באילו תנאים תלמיד שקיבל אפיון של לקות למידה יכול לקבל שעות סייעת? |
        |   | מי הם חברי הצוות הרב מקצועי? |
        """
    )
st.write('')
st.write('')
st.write('iftachts@gmail.com :ליצירת קשר')
