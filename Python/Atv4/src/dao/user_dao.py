import sqlite3
import random
import streamlit as st
from src.models.user import User

class UserDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./db/atvsql.db', check_same_thread=False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Clientes;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(id_usu = resultado[0], name = resultado[1], password = resultado[2], email=resultado[3]))
        self.cursor.close()
        return resultados

    def inserir_user(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Clientes(email, nome, senha)
            Values(?,?,?);
        """, (user.email, user.nome, user.password))
        self.conn.commit()
        self.cursor.close()

    def pegar_user(self, email):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Clientes
            WHERE email = '{email}';
        """)
        user  = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            user = (User(id_usu = resultado[0], name = resultado[1], password = resultado[2], email=resultado[3]))
        self.cursor.close()
        return user

    def atualizar_user(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Clientes SET
                name = '{user.name}',
                senha = {user.password}
                WHERE email = '{user.email}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_user(self, email):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Clientes 
                WHERE email = '{email}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def search_all_for_name(self, name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Clientes
            WHERE name LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(id_usu = resultado[0], name = resultado[1], password = resultado[2], email=resultado[3]))
        self.cursor.close()
        return resultados
    
    def search_all_for_email(self, email) -> bool:
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Clientes
            WHERE email LIKE '{email}%';
        """)
        for resultado in self.cursor.fetchall():
            if resultado[0] == email:
                return False
        self.cursor.close()
        return True

    def get_id(self) -> str:
        MAX_LIMIT = 255
        random_string = ''
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT id_cliente FROM Clientes
            WHERE id_cliente LIKE '{random_string}%';
        """)
        while True:
            for _ in range(3):
                random_integer = random.randint(0, MAX_LIMIT)
                random_string += (chr(random_integer))
            if random_string not in self.cursor.fetchall():
                break
        self.cursor.close()
        return random_string

    def novo_usu(self, user, senha, email) -> bool:
        if self.search_all_for_email(email):
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Clientes(id_cliente, email, nome, senha)
                Values(?,?,?,?);
            """, (self.get_id(), email, user, senha))
            self.conn.commit()
            self.cursor.close()
            st.session_state["Estado_Cadastro"] = "Concluido"
            return True
        st.session_state["Estado_Cadastro"] = "Email_Ig"
        return False