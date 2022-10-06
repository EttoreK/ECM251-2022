class Carr():
    def __init__(self):
        self._prods = []

    def adicionar(self, item):
        self._prods.append(item)

    def remover(self, item):
        self._prods.remove(item)
    
    def get_prods(self):
        return self._prods

    def limpa_carr(self):
        while len(self._prods) > 0:
            self._prods.pop()
        return self