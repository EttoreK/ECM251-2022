import sqlite3
import random
from src.models.item import Item

class ItemDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ItemDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./db/atvsql.db', check_same_thread=False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Itens;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Item(id_prod = resultado[0], nome = resultado[1], preco = resultado[2]))
        self.cursor.close()
        return resultados
    
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

    def inserir_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Itens(id, nome, preco)
            Values(?,?,?);
        """, (item.id, item.nome, item.preco))
        self.conn.commit()
        self.cursor.close()

    def pegar_item(self, id_prd):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE id = '{id_prd}';
        """)
        item  = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = (Item(id_prod = resultado[0], nome = resultado[1], preco = resultado[2]))
        self.cursor.close()
        return item

    def atualizar_item(self, item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Itens SET
                nome = '{item.nome}',
                preco = {item.preco}
                WHERE id = '{item.id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_item(self, id_prd):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Itens 
                WHERE id = '{id_prd}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def search_all_for_name(self, nome):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE nome LIKE '{nome}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Item(id_prod = resultado[0], nome = resultado[1], preco = resultado[2]))
        self.cursor.close()
        return resultados