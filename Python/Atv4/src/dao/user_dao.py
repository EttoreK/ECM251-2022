import sqlite3
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
            resultados.append(User(email = resultado[0], name = resultado[1], password = resultado[2]))
        self.cursor.close()
        return resultados

    def inserir_user(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Users(email, name, password)
            Values(?,?,?);
        """, (user.email, user.name, user.password))
        self.conn.commit()
        self.cursor.close()

    def pegar_user(self, email):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Users
            WHERE email = '{email}';
        """)
        user  = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            user = (User(email = resultado[0], name = resultado[1], password = resultado[2]))
        self.cursor.close()
        return user

    def atualizar_user(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Users SET
                name = '{user.name}',
                password = {user.password}
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
                DELETE FROM Users 
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
            SELECT * FROM Users
            WHERE name LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(email = resultado[0], name = resultado[1], password = resultado[2]))
        self.cursor.close()
        return resultados
    
    def search_all_for_email(self, email):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Users
            WHERE email LIKE '{email}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(email = resultado[0], name = resultado[1], password = resultado[2]))
        self.cursor.close()
        return resultados
    
    def novo_usu(self, user, senha, email) -> bool:
        if self.search_all_for_email(email) == None:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Users(email, name, password)
                Values(?,?,?);
            """, (email, user, senha))
            self.conn.commit()
            self.cursor.close()
            return True
        return False