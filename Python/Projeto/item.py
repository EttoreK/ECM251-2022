class Item():
    def __init__(self, preco, nome, descricao = None):
        self._nome = nome
        self._preco = preco
        self._descicao = descricao

    def get_nome(self):
        return self._nome
    
    def get_preco(self):
        return self._preco

    def get_desc(self):
        return self._descricao

    def __str__(self):
        return f'Nome: {self._nome} Preço: R${self._preco}'

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Item):
            return self._nome == __o.get_nome()
        return False