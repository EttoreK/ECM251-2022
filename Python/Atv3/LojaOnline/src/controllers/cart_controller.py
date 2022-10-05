import streamlit as st
from src.models.cart import Cart
from src.controllers.user_controller import UserController

class CartController():
    def __init__(self):
        self._cart = Cart()

    def add_product(self, product):
        if UserController().checklog():
            i = self._cart._products
            
            for j in range(len(i)):
                if i[j].get_name() != product.get_name():
                    self._cart._products.append(product)
                    return self
            
            if len(i) <= 0:
                self._cart._products.append(product)

            return self
        
        else:
            st.error("Faça Login na aba \"Perfil\" para adicionar ao carrinho")

    def tira_prod(self, name):
        products = self.get_cart().get_prod()
        for i in products:
           if name == i.get_name():
                products.remove(i)
                return self
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