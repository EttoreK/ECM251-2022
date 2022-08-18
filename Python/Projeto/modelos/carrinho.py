from produto import Produto

class Carrinho():
    def __init__(self):
        self._item = []

    def get_valor_total(self):
        total = 0
        for item in self._item:
            total += item.get_preco()
        return total

    def get_tamanho(self):
        return len(self._item)

    def adicionar(self, item):
        self._item.append(item)

    def remover(self, item):
        pass