from src.models.product import Product

class ProductController():
    def __init__(self):
        self._produtos = [
            Product("Pokemon", 400.00, "imgs/pkm.jpg"),
			Product("Yugioh", 40.00, "imgs/ygo.jpg"),
			Product("NoHero", 120.00, "imgs/mha.jpg"),
			Product("Digimon", 9.00, "imgs/dgm.jpg")
        ]

    def get_product(self, index):
        return self._produtos[index]