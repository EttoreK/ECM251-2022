class Item:
    def __init__(self, id_prod, nome, preco) -> None:
        self.id = id_prod
        self.nome = nome
        self.preco = preco
    
    def get_name(self):
        return self.nome
    
    def get_price(self):
        return self.preco
    
    def get_id(self):
        return self.id

    def get_img(self):
        return self._img
    
    def get_desc(self):
        return self._desc
    
    def __str__(self) -> str:
        return f'Item["id":{self.id}, "nome":{self.nome},preco":{self.preco}]"'