import streamlit as st
import time
import pyperclip
import platform

#######################
os_name = platform.system()
min_length = 3
link_url_mac = "https://dl.superapp.onprem.ru/downloads/mac/x64/latest/vkteams.dmg"


#######################
st.title("VK Teams")

st.write("Пожалуйста, введите данные для регистрации.")
username = st.text_input("Имя")
family = st.text_input("Фамилия")
checkbox = st.checkbox("Сгенерировать адрес почты автоматически")
input_block = st.empty()
if checkbox:
    col1, col2 = st.columns(([3, 1]))
    col1.empty()
    col2.empty()
    email = 'peppeer52'
else:
    col1, col2 = st.columns(([3, 1]))
    email1 = col1.text_input("Придумайте логин")
    domain = col2.text_input("Домен", value="@teams.onprem.ru", disabled=True)
password = st.text_input("Пароль", type="password")
confirm_password = st.text_input("Подтвердите пароль", type="password")

if st.button("Регистрация"):
    with st.spinner("Подключаюсь..."):
        # Здесь можно выполнить длительную операцию
        time.sleep(2)
    with st.spinner("Создаю учетную запись..."):
        # Здесь можно выполнить длительную операцию
        time.sleep(2)
    with st.spinner("Учетная запись создана"):
        # Здесь можно выполнить длительную операцию
        time.sleep(2)
    if checkbox:
        st.success(f"Ваш email: {email}, ваш пароль: {password}")
    else:
        st.success(f"Ваш email: " + email1 + domain + ", ваш пароль: " + password)
    if os_name == "Windows":
        st.write("Вы запустили приложение на Windows!")
    elif os_name == "Linux":
        st.write("Вы запустили приложение на Linux!")
    elif os_name == "Darwin":
        st.write("Вы запустили приложение на macOS!")
        if st.button("Скачать"):
            st.markdown(f'<a href="https://dl.superapp.onprem.ru/downloads/mac/x64/latest/vkteams.dmg" download>Скачать файл</a>', unsafe_allow_html=True)
    else:
        st.write(f"Вы запустили приложение на {os_name}!")