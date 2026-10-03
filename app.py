import streamlit as st
import random

st.set_page_config(page_title="Мій Супер-Додаток", page_icon="😁", layout="wide")
st.title("Ласкаво просимо до мого Додатку! 🚀")

tab1, tab2, tab3, tab4 = st.tabs(["Про мене", "Мій інструмент", "🔗 Корисні посилання", "🎮 Вгадай число"])

with tab1:
    st.header("Знайомство з автором")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/219/219988.png", width=200)
        
    with col2:
        st.header("Привіт! Я майбутній Python Developer!")
        st.write("Я навчаюсь в IT STEP. Створюю круті веб-додатки та вивчаю штучний інтелект.")
    
    with st.container():
        st.info("Контакту для зв'язку:")
        st.markdown("GitHub: [Діма (Сфіфн)](https://github.com)")
        st.markdown("Email: tssssssssdima@gmail.com")

with tab2:
    st.header("Корисний інструмент: Конвертер температури")
    st.write("Цей інструмент допоможе швидко перевести градуси Цельсія у Фаренгейти.")
    
    c1, c2 = st.columns(2)
    with c1:
     celsius = st.number_input("Введіть температуру в градусах Цельсія():", value=1.0, step=1.0)

with c2:
    fahrenheit = celsius * 1.8 + 32
    st.write(f"{fahrenheit} °F")



with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Ігри та розваги")
        st.markdown("[Lichess](https://lichess.org) — Безкоштовний шаховий сервер")
        st.markdown("[Roblox](https://roblox.com) — Ігрова онлайн-платформа")
        
    with col2:
        st.markdown("### Відео та навчання")
        st.markdown("[YouTube](https://youtube.com) — Відеохостинг для навчання та відпочинку")
        st.markdown("[Microsoft Teams](https://microsoft.com) — Платформа для командної роботи")

    

with tab4:
    st.header("🎮 Міні-гра: Вгадай число")
    st.write("Я загадав число від 1 до 100. Спробуй його відгадати!")

    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
    if "feedback" not in st.session_state:
        st.session_state.feedback = ""

    user_guess = st.number_input("Введіть ваше число:", min_value=1, max_value=100, step=1, key="game_guess")
    feedback_placeholder = st.empty()

    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        if st.button("Перевірити", type="primary"):
            if user_guess < st.session_state.secret_number:
                st.session_state.feedback = "📈 Загадане число більше!"
            elif user_guess > st.session_state.secret_number:
                st.session_state.feedback = "📉 Загадане число менше!"
            else:
                st.session_state.feedback = "🎉 Вітаємо! Ви вгадали!"

    with btn_col2:
        if st.button("Зіграти знову"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.feedback = "🔄 Загадано нове число! Спробуй відгадати."
            
    if st.session_state.feedback:
        if "Вітаємо" in st.session_state.feedback:
            feedback_placeholder.success(st.session_state.feedback)
        elif "Загадано нове число" in st.session_state.feedback:
            feedback_placeholder.info(st.session_state.feedback)
        else:
            feedback_placeholder.warning(st.session_state.feedback)
