import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(
    page_title="Ultimate Football Quiz 🏆", 
    page_icon="⚽", 
    layout="centered"
)

# تصميم CSS مخصص لاحترافية الواجهة
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    h1, h2, h3 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #00ffcc !important;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        border: none;
        box-shadow: 0px 4px 15px rgba(0, 114, 255, 0.4);
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0072ff 0%, #00c6ff 100%);
        box-shadow: 0px 6px 20px rgba(0, 114, 255, 0.6);
    }
    hr {
        border-color: #1f2937;
    }
    </style>
""", unsafe_allow_html=True)

# رأسية الموقع
st.image("https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=1200&auto=format&fit=crop", use_container_width=True)
st.title("⚽ ULTIMATE FOOTBALL QUIZ (40 QUESTIONS) ⚽")
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 18px;'>وضع التحدي المطور: السرعة والتركيز لصناعة أسطورة كروية جديدة!</p>", unsafe_allow_html=True)
st.divider()

# قاعدة بيانات الأسئلة
quiz_data = [
    {
        "q": "1. Who is the all-time top scorer of the UEFA Champions League?",
        "options": ["Lionel Messi", "Cristiano Ronaldo", "Robert Lewandowski", "Karim Benzema"],
        "answer": "Cristiano Ronaldo"
    },
    {
        "q": "2. Which country won the FIFA World Cup in 2022?",
        "options": ["Brazil", "Argentina", "France", "Germany"],
        "answer": "Argentina"
    },
    {
        "q": "3. How many minutes does a standard football match last?",
        "options": ["80 minutes", "90 minutes", "100 minutes", "120 minutes"],
        "answer": "90 minutes"
    },
    {
        "q": "4. Which nation has won the most FIFA World Cups in history?",
        "options": ["Germany", "Italy", "Argentina", "Brazil"],
        "answer": "Brazil"
    },
    {
        "q": "5. Which player is nicknamed 'CR7'?",
        "options": ["Lionel Messi", "Neymar Jr.", "Kylian Mbappe", "Cristiano Ronaldo"],
        "answer": "Cristiano Ronaldo"
    },
    {
        "q": "6. Which club plays against Barcelona in 'El Clasico'?",
        "options": ["Atletico Madrid", "Real Madrid", "Sevilla", "Valencia"],
        "answer": "Real Madrid"
    },
    {
        "q": "7. How many players from one team are on the pitch at the start of a match?",
        "options": ["10 players", "12 players", "11 players", "9 players"],
        "answer": "11 players"
    },
    {
        "q": "8. Who won the FIFA Ballon d'Or in 2023?",
        "options": ["Cristiano Ronaldo", "Kylian Mbappe", "Lionel Messi", "Robert Lewandowski"],
        "answer": "Lionel Messi"
    },
    {
        "q": "9. Which African team reached the World Cup semi-finals in Qatar 2022?",
        "options": ["Senegal", "Morocco", "Nigeria", "Ghana"],
        "answer": "Morocco"
    },
    {
        "q": "10. How many yellow cards lead to a red card in a single match?",
        "options": ["3 yellow cards", "2 yellow cards", "4 yellow cards", "5 yellow cards"],
        "answer": "2 yellow cards"
    },
    {
        "q": "11. Which player has won the most Ballon d'Or awards in history?",
        "options": ["Cristiano Ronaldo", "Johan Cruyff", "Lionel Messi", "Michel Platini"],
        "answer": "Lionel Messi"
    },
    {
        "q": "12. Which country won the first-ever FIFA World Cup in 1930?",
        "options": ["Argentina", "Brazil", "Uruguay", "Italy"],
        "answer": "Uruguay"
    },
    {
        "q": "13. Who is known as 'The King' (O Rei) in football history?",
        "options": ["Diego Maradona", "Zinedine Zidane", "Pele", "Ronaldinho"],
        "answer": "Pele"
    },
    {
        "q": "14. Which English club has won the most Premier League titles?",
        "options": ["Liverpool", "Manchester United", "Arsenal", "Manchester City"],
        "answer": "Manchester United"
    },
    {
        "q": "15. Which player transferred to PSG for a world-record fee of €222M in 2017?",
        "options": ["Kylian Mbappe", "Philippe Coutinho", "Neymar Jr.", "Jude Bellingham"],
        "answer": "Neymar Jr."
    },
    {
        "q": "16. Which stadium is known as the home of Real Madrid?",
        "options": ["Camp Nou", "Santiago Bernabeu", "San Siro", "Allianz Arena"],
        "answer": "Santiago Bernabeu"
    },
    {
        "q": "17. How many substitutions are typically allowed per team in a standard official match?",
        "options": ["3 substitutions", "4 substitutions", "5 substitutions", "6 substitutions"],
        "answer": "5 substitutions"
    },
    {
        "q": "18. Who scored the famous 'Hand of God' goal in 1986?",
        "options": ["Pele", "Mario Kempes", "Diego Maradona", "Ruud Gullit"],
        "answer": "Diego Maradona"
    },
    {
        "q": "19. Which manager led Manchester City to a Treble in the 2022-2023 season?",
        "options": ["Carlo Ancelotti", "Pep Guardiola", "Jurgen Klopp", "Jose Mourinho"],
        "answer": "Pep Guardiola"
    },
    {
        "q": "20. Which club is known as 'The Gunners'?",
        "options": ["Chelsea", "Tottenham", "Arsenal", "Aston Villa"],
        "answer": "Arsenal"
    },
    {
        "q": "21. Which country won UEFA Euro 2020 (played in 2021)?",
        "options": ["England", "Spain", "Italy", "Portugal"],
        "answer": "Italy"
    },
    {
        "q": "22. Who is the all-time top scorer for the Argentina national team?",
        "options": ["Gabriel Batistuta", "Lionel Messi", "Sergio Aguero", "Diego Maradona"],
        "answer": "Lionel Messi"
    },
    {
        "q": "23. Which Moroccan player won the UEFA Champions League with Chelsea in 2021?",
        "options": ["Achraf Hakimi", "Youssef En-Nesyri", "Hakim Ziyech", "Sofyan Amrabat"],
        "answer": "Hakim Ziyech"
    },
    {
        "q": "24. What is the distance (in yards) from the penalty spot to the goal line?",
        "options": ["10 yards", "15 yards", "12 yards", "18 yards"],
        "answer": "12 yards"
    },
    {
        "q": "25. Which club has won the most UEFA Champions League titles?",
        "options": ["AC Milan", "Real Madrid", "Bayern Munich", "Liverpool"],
        "answer": "Real Madrid"
    },
    {
        "q": "26. Which country hosted the 2010 FIFA World Cup?",
        "options": ["Brazil", "Germany", "South Africa", "Russia"],
        "answer": "South Africa"
    },
    {
        "q": "27. Who won the Golden Boot at the 2022 FIFA World Cup?",
        "options": ["Lionel Messi", "Kylian Mbappe", "Olivier Giroud", "Julian Alvarez"],
        "answer": "Kylian Mbappe"
    },
    {
        "q": "28. Which Italian club is nicknamed 'The Old Lady' (La Vecchia Signora)?",
        "options": ["AC Milan", "Inter Milan", "Juventus", "AS Roma"],
        "answer": "Juventus"
    },
    {
        "q": "29. How long is extra time in a knockout match (two halves total)?",
        "options": ["15 minutes", "30 minutes", "20 minutes", "40 minutes"],
        "answer": "30 minutes"
    },
    {
        "q": "30. Which player is nicknamed 'El Pulga'?",
        "options": ["Sergio Aguero", "Alexis Sanchez", "Lionel Messi", "Paulo Dybala"],
        "answer": "Lionel Messi"
    },
    {
        "q": "31. Who won the FIFA Women's World Cup in 2023?",
        "options": ["England", "USA", "Spain", "Sweden"],
        "answer": "Spain"
    },
    {
        "q": "32. Which country won the Africa Cup of Nations (AFCON) in 2021 (played in 2022)?",
        "options": ["Egypt", "Senegal", "Algeria", "Cameroon"],
        "answer": "Senegal"
    },
    {
        "q": "33. Which player wore the iconic number 7 shirt at Manchester United before Ronaldo?",
        "options": ["Eric Cantona", "George Best", "David Beckham", "Wayne Rooney"],
        "answer": "David Beckham"
    },
    {
        "q": "34. Which stadium is the home ground of FC Barcelona?",
        "options": ["Santiago Bernabeu", "Camp Nou", "Metropolitano", "Mestalla"],
        "answer": "Camp Nou"
    },
    {
        "q": "35. Who holds the record for the most official goals scored in a single calendar year (91 goals)?",
        "options": ["Cristiano Ronaldo", "Gerd Muller", "Lionel Messi", "Pele"],
        "answer": "Lionel Messi"
    },
    {
        "q": "36. Which German club is famous for winning 11 consecutive Bundesliga titles?",
        "options": ["Borussia Dortmund", "Bayern Munich", "Bayer Leverkusen", "RB Leipzig"],
        "answer": "Bayern Munich"
    },
    {
        "q": "37. What color card is shown to a player who is immediately sent off?",
        "options": ["Yellow card", "Green card", "Red card", "Blue card"],
        "answer": "Red card"
    },
    {
        "q": "38. Who was the captain of the Morocco national team at the 2022 World Cup?",
        "options": ["Achraf Hakimi", "Romain Saiss", "Yassine Bounou", "Hakim Ziyech"],
        "answer": "Romain Saiss"
    },
    {
        "q": "39. Which player won the FIFA World Cup with Brazil in 2002 and the Ballon d'Or in 2005?",
        "options": ["Ronaldo Nazario", "Ronaldinho", "Kaka", "Rivaldo"],
        "answer": "Ronaldinho"
    },
    {
        "q": "40. Which country will co-host the 2026 FIFA World Cup alongside USA and Mexico?",
        "options": ["Brazil", "Canada", "Spain", "England"],
        "answer": "Canada"
    }
]

# تتبع الوقت البداية
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# فورم الأسئلة
with st.form("ultimate_quiz_form"):
    user_answers = {}
    
    for i, item in enumerate(quiz_data):
        st.markdown(f"### {item['q']}")
        user_answers[i] = st.radio("اختر الإجابة المناسبة:", item["options"], key=f"q_{i}", index=None)
        st.markdown("---")
        
    submitted = st.form_submit_button("إرسال النتائج النهائية 🚀")

# حساب النتيجة
if submitted:
    if None in user_answers.values():
        st.warning("⚠️ عافاك جاوب على جميع الأسئلة عاد صيفط النتائج!")
    else:
        end_time = time.time()
        total_time = round(end_time - st.session_state.start_time, 2)
        
        score = 0
        for i, item in enumerate(quiz_data):
            if user_answers[i] == item["answer"]:
                score += 1
                
        percentage = int((score / len(quiz_data)) * 100)

        st.balloons()
        st.header("📊 التقرير النهائي للنتيجة")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("🎯 النقطة", f"{score} / {len(quiz_data)}")
        col2.metric("📈 النسبة", f"{percentage}%")
        col3.metric("⏱️ الوقت", f"{total_time} ث")

        st.divider()

        if percentage == 100:
            st.success("🏆 أسطورة مطلقة! علّامة في عالم كرة القدم!")
        elif percentage >= 75:
            st.success("🔥 مستوى عالي جداً، تبارك الله عليك!")
        elif percentage >= 50:
            st.info("👍 نتيجة مقبولة، واصل التطور!")
        else:
            st.error("😅 حاول مرة أخرى لرفع ثقافتك الكروية!")
            
        st.session_state.start_time = time.time()