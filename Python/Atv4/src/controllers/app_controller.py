from src.controllers.item_controller import ItemController
from src.controllers.cart_controller import CarrController

class Application:
	def __init__(self):
		self.item_controller = ItemController()
		self.pedido_controller = CarrController()
		self.cliente_pedido_atual = None
	
	def listar_itens(self):
		return self.item_controller.pegar_todos_itens()
	
	def visualizar_pedido(self):
		retorno = {
			"id_cliente" : self.cliente_pedido_atual.id_cliente,
			"data" : self.cliente_pedido_atual.data,
			"items" : []
		}

		itens_pedido = self.pedido_controller.pegar_pedido(self.cliente_pedido_atual.id_pedido)

		for item in itens_pedido:
			item_data = self.item_controller.pegar_item(item.id_item)
			retorno["items"].append({"nome":item_data.nome, "preco":item_data.preco, "quantidade":item.quantidade})
		return retorno
	
	def fechar_pedido(self):
		return self.pedido_controller.total_pedido(self.cliente_pedido_atual.id_pedido)