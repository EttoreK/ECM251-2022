from src.models.cart import Cart
from src.models.product import Product

class CartController():
    def __init__(self):
        self._cart = Cart()

    def add_product(self, product):
        i = self._cart._products
        for j in range(len(i)):
            if i[j].get_name() == product.get_name():
                return

        self._cart._products.append(product)
        print(self._cart._products)
        return self

    def calculate_price(self,product):
        return (product.get_price())

    def get_cart(self):
        return self._cart

    def total_price(self):
        products = self.get_cart().get_prod()
        total = 0
        for i in products:
           total += (i.get_price())
        return total
	
    def get_prod(self):
        return self._cart._products
