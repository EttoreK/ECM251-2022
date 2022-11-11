import streamlit as st
from src.dao.user_dao import UserDAO
from src.models.user import User

class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = UserDAO.get_instance().get_all()
    
    def check_user(self,user):
        return user in self.users

    def check_login(self, name, password):
        user_test = User(id_usu = "𖥸", name = name, password = password, email="𖥸")
        for user in self.users:
            if (user.get_name() == user_test.get_name() or user.get_email() == user_test.get_name()) and user.get_password() == user_test.get_password():
                st.session_state['Login'] = "aprovado"
                st.session_state['Usuario'] = user.get_name()
                st.session_state['Email'] = user.get_email()
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
    
    def cadastrar(self, name, senha, senha2, email) -> bool:
        retorno = False
        if senha == "" or senha2 == "" or name == "" or email == "":
            st.session_state["Estado_Cadastro"] = "Senha_Vaz"
            return retorno
        if senha != senha2:
            st.session_state["Estado_Cadastro"] = "Senha_Dispar"
            return retorno
        retorno = UserDAO.get_instance().novo_usu(name, senha, email)
        return retorno
