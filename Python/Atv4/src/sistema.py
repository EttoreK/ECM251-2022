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
		st.set_page_config(layout='wide')

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
		if not id:
			id = self.itemc.pegar_id()
		if not nome or not preco:
			st.error("Preenha todos os campos (\"Nome\", \"Preco\")")
			return
		self.itemc.inserir_item(Item(id, nome, preco))
	
	def verifica_adm(self) -> bool:
		return self.userc.check_adm()
	
	def verifica_login(self, user, senha) -> None:
		self.userc.check_login(user,senha)

	def inverte_estado_cadastro(self) -> None:
		st.session_state["Cadastro"] = not st.session_state["Cadastro"]

	def realiza_cadastro(self,user,password,password2,email) -> None:
		self.userc.cadastrar(user,password,password2,email)
	
	def altera_usuario(self, nome_usu, email_usu, senha_usu, senha_usu2) -> None:
		user = self.userc.usuario_atual()
		novo_nome = user.get_name()
		novo_email = user.get_email()
		nova_senha = user.get_password()

		if senha_usu2 != senha_usu:
			st.error("As senhas devem ser iguais")
			return
		elif senha_usu2 == user.get_password() or senha_usu == user.get_password():
			st.error("As senhas não podem ser igauis à anterior")
			return
		elif senha_usu != user.get_password() and senha_usu != "":
			nova_senha = senha_usu

		if nome_usu != user.get_name() and nome_usu != "":
			novo_nome = nome_usu
		
		if email_usu != user.get_email() and email_usu != "":
			novo_email = email_usu
		
		novo_usu = self.userc.usuario_fantasma(st.session_state['Id'], novo_nome, nova_senha, novo_email)
		
		alterdo = self.userc.alterar_usuario(novo_usu)
		if alterdo:
			st.error("Alterado com sucesso")
		else:
			st.error("Falha ao alterar")
	
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
