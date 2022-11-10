from src.controllers.app_controller import Application
import streamlit as st

class Sistema:
	def __init__(self) -> None:
		self.app = Application()
		self.continuar = True

	def sair(self):
		self.continuar = False

	def criar_pedido(self):
		cpf = input("CPF: ")
		self.app.criar_novo_pedido(cpf=cpf)

	def exibir_itens(self):
		for item in self.app.listar_itens():
			print(item)
		
	def adicionar_item(self):
		id = input("Item ID:")
		quantidade_ins = int(input("Quantidade:"))
		self.app.adicionar_item_no_pedido(id_item=id, quantidade_item=quantidade_ins)
	
	def visualizar_pedido(self):
		print(self.app.visualizar_pedido())

	def total_pedido(self):
		print(self.app.fechar_pedido())

	def run(self):
		while self.continuar:
			opcao = input()
			if opcao not in self.acoes.keys():
				print("Opcao Invalida")
				continue
			self.acoes[opcao]()
	
	def get_key(self) -> int:
		if "Key" not in st.session_state:
			st.session_state["Key"] = 0
		else:
			st.session_state["Key"] += 1
			if st.session_state["Key"] > 40:
				st.session_state["Key"] = 0
		
		return st.session_state["Key"]
	
	def inverte(self):
		st.session_state["Cadastro"] = not st.session_state["Cadastro"]
		