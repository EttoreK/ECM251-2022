import streamlit as st
from src.models.user import User

class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = [
            User(name="Datman", password = "robin", email = "druce_vvayne@yahoo.com.br"),
            User(name="JoãoRuimdeBriga", password = "arroz2", email = "joao.briga@gmail.com"),
            User(name ="Tais", password="petacular", email = "tais.perando@ali.co")
        ]
    
    def check_user(self,user):
        return user in self.users

    def check_login(self, name, password):
        user_test = User(name = name, password = password, email=None)
        for user in self.users:
            if (user.get_name() == user_test.get_name() or user.get_email() == user_test.get_name()) and user.get_password() == user_test.get_password():
                st.session_state['Login'] = "aprovado"
                st.session_state['Usuario'] = user.get_name()
                st.session_state['email'] = user.get_email()
                return True
        return False
    
    def checklog(self):
        if st.session_state['Login'] == "aprovado":
            return True
        else:
            return False

    def logout(self, kart):
        st.session_state["Login"] = "negado"
        kart.get_carr().limpa_carr()
