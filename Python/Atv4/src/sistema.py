import streamlit as st
from src.controllers.app_controller import Application
from src.controllers.cart_controller import CarrController
from src.controllers.item_controller import ItemController
from src.controllers.user_controller import UserController
from src.models.item import Item

class Sistema:
	def __init__(self) -> None:
		self.app = Application()
		self.itemc = ItemController()
		self.carrc = CarrController()
		self.userc = UserController()
	
	def comeco(self) -> None:
		if "Cadastro" not in st.session_state:
			st.session_state["Cadastro"] = False
			st.session_state["Estado_Cadastro"] = ""

		if "Login" not in st.session_state:
			st.session_state["Login"] = "negado"
			st.session_state["Usuario"] = ""
			st.session_state["Email"] = ""
			st.session_state['Id'] = ""
			st.session_state["Carr"] = CarrController()
	
	def get_key(self) -> int:
		if "Key" not in st.session_state:
			st.session_state["Key"] = 0
		else:
			st.session_state["Key"] += 1
			if st.session_state["Key"] > 40:
				st.session_state["Key"] = 0
		
		return st.session_state["Key"]
	
	def pega_item(self, item) -> Item:
		return self.itemc.pegar_item(item)

	def add_produto_carr(self, carrinho, prodct) -> None:
		return CarrController.add_prod(st.session_state['Carr'], prodct)
	
	def add_produto_db(self, id, nome, preco) -> None:
		if id == "":
			id = self.itemc.pegar_id()
		self.itemc.inserir_item(Item(id, nome, preco))
	
	def verifica_adm(self) -> bool:
		return self.userc.check_adm()
	
	def verifica_login(self, user, senha) -> None:
		self.userc.check_login(user,senha)

	def inverte_estado_cadastro() -> None:
		st.session_state["Cadastro"] = not st.session_state["Cadastro"]

	def realiza_cadastro(self,user,password,password2,email) -> None:
		self.userc.cadastrar(user,password,password2,email)
	
	def sair(self) -> None:
		self.userc.logout(st.session_state["Carr"])

	def pega_produtos_carrinho(self) -> list:
		return st.session_state["Carr"].get_prod()
	
	def pega_prod_nome(self, item) -> str:
		return item.get_name()

	def pega_prod_preco(self, item) -> float:
		return item.get_price()

	def remove_produto_carrinho(self, carrinho, item) -> None:
		st.session_state['Carr'].tira_prod(item.get_name())
	
	def preco_total(self) -> float:
		return st.session_state['Carr'].ttl_cust()
