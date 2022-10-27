import streamlit as st
from src.controllers.app_controller import Application
from src.controllers.cart_controller import CarrController
from src.controllers.item_controller import ItemController
from src.controllers.user_controller import UserController

class Sistema:
	def __init__(self) -> None:
		self.app = Application()
		self.continuar = True
		self.acoes = {
			"0":self.sair,
			"1":self.criar_pedido,
			"2":self.exibir_itens,
			"3":self.adicionar_item,
			"4":self.visualizar_pedido,
			"5":self.total_pedido
		}

	def menu(self):
		print("1 - Criar novo pedido")
		print("2 - Exibir itens")
		print("3 - Adicionar item")
		print("4 - Visualizar pedidos")
		print("5 - Total do pedido")
		print("0 - Sair")

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
			self.menu()
			opcao = input()
			if opcao not in self.acoes.keys():
				print("Opcao Invalida")
				continue
			self.acoes[opcao]()

	with open("./css/style.css") as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

	if 'Carr' not in st.session_state:
		st.session_state['Carr'] = CarrController()

	p_contr = ItemController()
	tab1, tab2, tab3 = st.tabs(["Início", "Perfil", "Carrinho"])

	with tab1:
		# Titulo
		st.header("Início")

		# mostruario
		st.markdown("###### Pókemon")
		st.image(image = "imgs/pkm.jpg", width=700)
		col1, col2, col3 = st.columns(3,gap="large")
		with col1: 
			st.markdown("#### R$ 400,00")
		with col2:
			st.markdown("#### mais de 1000 episódios para assistir")
		with col3:
			prdct = p_contr.pegar_item(0)
			c = st.container()
			c.button(label = "Adicionar", key = 0, on_click = CarrController.add_prod, args = (st.session_state['Carr'],prdct))

		col1, col2, col3 = st.columns(3,gap="large")
		
		with col1:
			prdct = p_contr.pegar_item(1)
			c = st.container()
			c.markdown("###### Yu-Gi-Oh! Duel Monsters")
			c.image("imgs/ygo.jpg", width=200)
			c.markdown("\r#### R$ 40,00")
			c.markdown("#### 224 episódios para assistir")
			c.button(label = "Adicionar", key = 1, on_click = CarrController.add_prod, args = (st.session_state['Carr'],prdct))
				

		with col2:
			prdct = p_contr.pegar_item(2)
			print(prdct)
			c = st.container()
			c.markdown("###### My hero Academia")
			c.image("imgs/mha.jpg", width=200)
			c.markdown("\r#### R$ 120,00")
			c.markdown("#### 113 episódios para assistir")
			c.button(label = "Adicionar", key = 2, on_click = CarrController.add_prod, args = (st.session_state['Carr'],prdct))

		with col3:
			prdct = p_contr.pegar_item(3)
			c = st.container()
			c.markdown("###### Digimon")
			c.image("imgs/dgm.jpg", width=200)
			c.markdown("\r\n#### R$ 9,00")
			c.markdown("#### Vários episódios para assistir")
			c.button(label = "Adicionar", key = 3, on_click = CarrController.add_prod, args = (st.session_state['Carr'],prdct))
		
	with tab2:
		if "Login" not in st.session_state:
			st.session_state["Login"] = "negado"
			st.session_state["Usuario"] = ""
			st.session_state["email"] = ""

		if st.session_state["Login"] != "aprovado":
			st.header("Login")
			user = st.text_input(
				label="",
				placeholder="Usuário"
			)
			password = st.text_input(
				label="",
				placeholder="Senha",
				type = "password"
			)
			col1, col2 = st.columns(2)
			with col1:
				st.button(label= "Entrar", key = 4, on_click= UserController.check_login, args = (UserController(),user,password))
			with col2:
				if st.button(label= "Criar conta", key = 5, on_click= None):
					st.markdown("Opção indisponível")
		else:
			st.header("Perfil")

			col1, col2 = st.columns(2)

			with col1:
				st.image(image="imgs/us.jpg", width=350)
				
			with col2:
				st.markdown(f"### Nome:\n{st.session_state['Usuario']}")
				st.markdown(f"### Email:\n{st.session_state['email']}")
			
			st.button(label= "Sair", key = 6, on_click= UserController.logout, args=(UserController(), st.session_state['Carr']))

	with tab3:
		if 'Carr' in st.session_state:

			row = st.container()
			col1,col2,col3 = st.columns(3)
			col1.markdown("##### Produto")
			col2.markdown("##### Preço")
			col3.markdown("##### Excluir\n\n\n")
			prods = st.session_state['Carr'].get_carr().get_prods()
			with row :
				i = 7
				for i in prods:
					col1.markdown("#### %s" % i.get_name())
					col2.markdown("#### R\$ %.2f" % i.get_price())
					col3.button(label= "Remover", key = i , on_click=CarrController.tira_prod , args=(st.session_state['Carr'],i.get_name()))
					i =+ 1

			col1, col2 = st.columns(2)

			col1.markdown("### Preço Total:")
			col2.markdown("### R\$ %.2f" % st.session_state['Carr'].ttl_cust())