import streamlit as st
from src.models.cart import Carr
from src.controllers.user_controller import UserController

class CarrController():
    def __init__(self):
        self._carr = Carr()

    def add_prod(self, prod):
        if UserController().checklog():
            i = self._carr._prods
            
            for j in range(len(i)):
                if i[j].get_name() != prod.get_name():
                    self._carr._prods.append(prod)
                    return self
            
            if len(i) <= 0:
                self._carr._prods.append(prod)

            return self
        
        else:
            st.error("Faça Login na aba \"Perfil\" para adicionar ao carrinho")

    def tira_prod(self, name):
        prods = self.get_carr().get_prods()
        for i in prods:
           if name == i.get_name():
                prods.remove(i)
                return self
        return self

    def get_carr(self):
        return self._carr

    def get_prod(self):
        return self._carr._prods

    def ttl_cust(self):
        prods = self.get_carr().get_prods()
        total = 0
        for i in prods:
           total += (i.get_price())
        return total