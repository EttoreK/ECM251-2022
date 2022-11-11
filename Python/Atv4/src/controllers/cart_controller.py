import streamlit as st
from src.controllers.user_controller import UserController
from src.controllers.item_controller import ItemController
from src.dao.pedido_dao import PedidoDAO
from src.models.cart import Carr

class CarrController():
    def __init__(self):
        self._carr = Carr()

    def add_prod(self, prod):
        if UserController().checklog():
            Cprod = self.get_prod()
            
            try:
                len(Cprod) > 0
            except:
                Cprod.append(prod)
                return self

            listid = Cprod
            # print(len(Cprod))
            for j in range(len(Cprod)):
                listid[j] = Cprod[j]

            if prod.get_id() not in listid:
                Cprod.append(prod)

            return Cprod
        
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
        return self._carr.get_prods()

    def ttl_cust(self):
        Cprod = self.get_prod()
        total = 0
        for i in Cprod:
           total += (i.get_price())
        return total
    
    def total_pedido(self, numero_pedido) -> float:
        items_pedido = PedidoDAO.get_instance().pegar_pedido(numero_pedido)
        total = 0
        item_controller = ItemController()
        for item in items_pedido:
            item_elemento = item_controller.pegar_item(item.id_item)
            total += item_elemento.preco * item.quantidade
        return total

    def pegar_pedido(self, numero_pedido)-> list:
        return PedidoDAO.get_instance().pegar_pedido(numero_pedido)

    def atualizar_pedido(self, pedido)-> bool:
        return PedidoDAO.get_instance().atualizar_pedido(pedido)

    def deletar_pedido(self, id) -> bool:
        return PedidoDAO.get_instance().deletar_item(id)

    def inserir_pedido(self, pedido) -> None:
        PedidoDAO.get_instance().inserir_pedido(pedido)