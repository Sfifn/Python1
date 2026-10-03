import streamlit as st

st.set_page_config(page_title="Мой сайт на Streamlit", layout="centered")

tab1, tab2 = st.tabs(["Профиль / Контакты", "Конвертер температур"])

with tab1:
    with st.container():
        st.info("Контакти для зв'язку:")
        st.markdown("GitHub: [USERNAME](https://github.com)")
        st.markdown("Email: XXXXXXX@itstep.org")

with tab2:
    st.header("Корисний інструмент: Конвертер температури")
    st.write("Цей інструмент допоможе швидко перевести градуси Цельсія у Фаренгейти.")
    
    c1, c2 = st.columns(2)
    
    with c1:
        celsius = st.number_input("Введіть температуру в градусах Цельсія:", value=0.0)

    with c2:

        fahrenheit = celsius * 1.8 + 32
        
        st.metric(label="Температура в Фаренгейтах:", value=f"{fahrenheit:.1f} °F")
