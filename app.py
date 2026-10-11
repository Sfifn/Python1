import streamlit as st

st.title("🎮 Застосунок GameMatch")

tab1, tab2, tab3 = st.tabs(["🕹️ Поиск ігор", "💵 Курс валют", "🌡️ Градуси"])

with tab1:
    st.header("Поиск и жанри ігор")
    
    poisk = st.text_input("Введіть назву гри для пошуку:")
    
    games = [
        {"name": "Minecraft", "genre": "Пісочниця, Виживання", "type": "Платна", "link": "https://minecraft.net"},
        {"name": "Dota 2", "genre": "MOBA, Стратегия", "type": "Безкоштовна", "link": "https://dota2.com"},
        {"name": "Counter-Strike 2", "genre": "Тактичний Шутер", "type": "Безкоштовна", "link": "https://counter-strike.net"},
        {"name": "The Witcher 3", "genre": "RPG, Відкритий світ", "type": "Платна", "link": "https://thewitcher.com"},
        {"name": "Cyberpunk 2077", "genre": "Action RPG", "type": "Платна", "link": "https://cyberpunk.net"},
        {"name": "GTA V", "genre": "Екшен-пригода", "type": "Платна", "link": "https://rockstargames.com"},
        {"name": "Roblox", "genre": "Песочниця", "type": "Безкоштовна", "link": "https://roblox.com"},
        {"name": "League of Legends", "genre": "MOBA", "type": "Безкоштовна", "link": "https://leagueoflegends.com"},
        {"name": "Valorant", "genre": "Тактичний шутер", "type": "Безкоштовна", "link": "https://playvalorant.com"},
        {"name": "Apex Legends", "genre": "Королівська битва", "type": "Безкоштовна", "link": "https://ea.com"}
    ]
    
    for game in games:
        if poisk.lower() in game["name"].lower():
            st.subheader(game["name"])
            st.write(f"Жанр: {game['genre']}")
            st.write(f"Тип: **{game['type']}**")
            st.markdown(f"[➔ Перейти на сайт]({game['link']})")
            st.write("---")

with tab2:
    st.header("Конвертер валют у Гривні (UAH)")
    
    amount = st.number_input("Введіть кількість валюти:", min_value=1, value=1, step=1)
    usd = round(amount * 41.50, 1)
    eur = round(amount * 45.20, 1)
    gbp = round(amount * 54.10, 1)
    pln = round(amount * 10.40, 1)
    cad = round(amount * 30.20, 1)
    
    # Теперь просто выводим их на экран без всяких сложных двоеточий
    st.write(f"**USD (Долар США):** {usd} грн.")
    st.write(f"**EUR (Евро):** {eur} грн.")
    st.write(f"**GBP (Фунт):** {gbp} грн.")
    st.write(f"**PLN (Злотий):** {pln} грн.")
    st.write(f"**CAD (Канадський долар):** {cad} грн.")
    
    
with tab3:
    st.header("Переведення Цельсія у Фаренгейт")
    
    celsius = st.number_input("Градуси Цельсія (°C):", value=1.0, step=0.1)
    
    fahrenheit = (celsius * 9/5) + 32
    
    st.write(f"### Результат: {fahrenheit:.1f} °F")
