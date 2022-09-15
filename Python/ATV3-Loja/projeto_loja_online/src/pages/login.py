from pickle import TRUE
from turtle import onclick
import streamlit as st
from controllers.user_controller import UserController

st.title(
    body = "Login", 
    anchor = None
)

# st.markdown("***")

user_name = st.text_input(
    label="",
    placeholder="Nome de usuário"
)

password = st.text_input(
    label= "",
    type="password",
    placeholder= "Senha"
)

button1 = st.button(
    label= "Entrar",
    on_click = UserController.login,
    kwargs={"user":user_name, "password":password}
)

Stts = ""
if(password!="" and user_name!=""):
    Stts = UserController.login(user_name, password)
    if(Stts == "L"):
        st.caption("Entrou")
    else:
        st.caption("Usuário ou senha incorretos")
else:
    st.caption("Preencha as informações")