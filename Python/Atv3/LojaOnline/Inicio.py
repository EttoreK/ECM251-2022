import streamlit as st
from src.controllers.cart_controller import CartController
from src.models.product import Product
from src.controllers.user_controller import UserController
from src.models.cart import Cart

with open("src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Início", "Perfil", "Carrinho"])

with tab1:
     # Titulo
	st.header("Início")
	
	# Painel lateral
	global Kart
	Kart = Cart()
	product1 = Product("Pokemon", 400.00, "imgs/pkm.jpg")
	product2 = Product("Yugioh", 40.00, "imgs/ygo.jpg")
	product3 = Product("NoHero", 120.00, "imgs/mha.jpg")
	product4 = Product("Digimon", 9.00, "imgs/dgm.jpg")

	# mostruario
	st.markdown("###### Pókemon")
	st.image(image = "imgs/pkm.jpg", width=700)
	st.markdown("#### R$ 400,00 \r mais de 1000 episódios para assistir")

	col1, col2, col3 = st.columns(3,gap="large")
	
	with col1:
			c = st.container()
			c.markdown("###### Yu-Gi-Oh! Duel Monsters")
			c.image("imgs/ygo.jpg", width=200)
			c.markdown("\r#### R$ 40,00")
			c.markdown("#### 224 episódios para assistir")
			if c.button(label = "Adicionar", key = 1, on_click = Cart.adicionar, args = (Kart,product2)):
				Kart.adicionar(product2)

	with col2:
			c = st.container()
			c.markdown("###### My hero Academia")
			c.image("imgs/mha.jpg", width=200)
			c.markdown("\r#### R$ 120,00")
			c.markdown("#### 113 episódios para assistir")
			if c.button(label = "Adicionar", key = 2, on_click = Cart.adicionar, args = (Kart,product3)):
				Kart.adicionar(product3)

	with col3:
			c = st.container()
			c.markdown("###### Digimon")
			c.image("imgs/dgm.jpg", width=200)
			c.markdown("\r\n#### R$ 9,00")
			c.markdown("#### Vários episódios para assistir")
			if c.button(label = "Adicionar", key = 3, on_click = Cart.adicionar, args = (Kart,product4)):
				Kart.adicionar(product4)

with tab2:
	user = ''
	password = ''

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
			st.button(label= "Entrar", on_click= UserController.check_login, args = (UserController(),user,password))
		with col2:
			st.button(label= "Criar conta", key = 4, on_click=None)

	else:
		st.header("Perfil")

		col1, col2 = st.columns(2)

		with col1:
			st.image(image="imgs/us.jpg", width=350)
			
		with col2:
			st.markdown(f"### Nome:\n{st.session_state['Usuario']}")
			st.markdown(f"### Email:\n{st.session_state['Email']}")
		
		st.button(label= "Sair", key = 5, on_click= UserController.logout)

with tab3:
	def prodprec(int):
		c = st.container()
		for i in Kart.get_prod():
			if int == 0:
				c.markdown(i.get_name())
			elif int == 1:
				c.markdown(i.get_price())
			elif int == 2:
				c.image(i.get_url(), width=100)
		return c

	st.header("Carrinho")
	col1, col2, col3 = st.columns(3)
	with col1:
		prodprec(0)
	with col2:
		prodprec(1)
	with col3:
		prodprec(2)
