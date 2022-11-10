class Item:
    def __init__(self, id, nome, preco) -> None:
        self.id = id
        self.nome = nome
        self.preco = preco
        self._img = ""
        self._desc = "Bom dia"
    
    def get_name(self):
        return self.nome
    
    def get_price(self):
        return self.preco

    def get_img(self):
        return self._img
    
    def get_desc(self):
        return self._desc
    
    def __str__(self) -> str:
        return f'Item["id":{self.id}, "nome":{self.nome},preco":{self.preco}]"'