import streamlit as st
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
	Kart = Cart()
	product1 = Product("Pokemon", 400.00, "https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/aGhopp3MHppi7kooGE2Dtt8C.png")
	product2 = Product("Yugioh", 40.00, "https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/aGhopp3MHppi7kooGE2Dtt8C.png")

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
			c.button(label = "Adicionar", key = 1, on_click = Kart.adicionar(item = product1))

	with col2:
			c = st.container()
			c.markdown("###### My hero Academia")
			c.image("imgs/mha.jpg", width=200)
			c.markdown("\r#### R$ 120,00")
			c.markdown("#### 113 episódios para assistir")
			c.button(label = "Adicionar", key = 2, on_click = Kart.adicionar(item = product1))

	with col3:
			c = st.container()
			c.markdown("###### Digimon")
			c.image("imgs/dgm.jpg", width=200)
			c.markdown("\r\n#### R$ 9,00")
			c.markdown("#### Vários episódios para assistir")
			c.button(label = "Adicionar", key = 3, on_click = Kart.adicionar(item = product1))

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
	def prodprec():
		col1, col2 = st.columns(2)
		c = st.container()
		for i in Kart.get_prod():
			with col1:
				c.markdown(i.get_name())
			with col2:
				c.markdown(i.get_price())
		return c

	st.header("Carrinho")
	st.button(label= "Prod", key = 6, on_click = prodprec)