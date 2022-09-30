import streamlit as st
from src.controllers.cart_controller import CartController
from src.controllers.user_controller import UserController
from src.controllers.product_controller import ProductController

with open("src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

p_contr = ProductController()
if 'Cart' not in st.session_state:
	st.session_state['Cart'] = CartController()
	Kart = st.session_state['Cart']

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
		prdct = p_contr.get_product(0)
		c = st.container()
		c.button(label = "Adicionar", key = 0, on_click = CartController.add_product, args = (st.session_state['Cart'],prdct))

	col1, col2, col3 = st.columns(3,gap="large")
	
	with col1:
		prdct = p_contr.get_product(1)
		c = st.container()
		c.markdown("###### Yu-Gi-Oh! Duel Monsters")
		c.image("imgs/ygo.jpg", width=200)
		c.markdown("\r#### R$ 40,00")
		c.markdown("#### 224 episódios para assistir")
		c.button(label = "Adicionar", key = 1, on_click = CartController.add_product, args = (st.session_state['Cart'],prdct))
			

	with col2:
		prdct = p_contr.get_product(2)
		print(prdct)
		c = st.container()
		c.markdown("###### My hero Academia")
		c.image("imgs/mha.jpg", width=200)
		c.markdown("\r#### R$ 120,00")
		c.markdown("#### 113 episódios para assistir")
		c.button(label = "Adicionar", key = 2, on_click = CartController.add_product, args = (st.session_state['Cart'],prdct))

	with col3:
		prdct = p_contr.get_product(3)
		c = st.container()
		c.markdown("###### Digimon")
		c.image("imgs/dgm.jpg", width=200)
		c.markdown("\r\n#### R$ 9,00")
		c.markdown("#### Vários episódios para assistir")
		c.button(label = "Adicionar", key = 3, on_click = CartController.add_product, args = (st.session_state['Cart'],prdct))
	
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
			if st.button(label= "Criar conta", key = 5, on_click=None):
				st.markdown("Opção indisponível")

	else:
		st.header("Perfil")

		col1, col2 = st.columns(2)

		with col1:
			st.image(image="imgs/us.jpg", width=350)
			
		with col2:
			st.markdown(f"### Nome:\n{st.session_state['Usuario']}")
			st.markdown(f"### Email:\n{st.session_state['email']}")
		
		st.button(label= "Sair", key = 6, on_click= UserController.logout)

with tab3:
	if 'Cart' in st.session_state:

		row = st.container()
		col1,col2 = st.columns(2)
		col1.markdown("##### Produto")
		col2.markdown("##### Preço")
		prods = st.session_state['Cart'].get_cart().get_prod()
		with row :
			for i in prods:
				col1.markdown("#### %s" % i.get_name())
				col2.markdown("#### R\$ %.2f" % i.get_price())

		col1,col2 = st.columns(2)

		col1.markdown("### Preço Total:")
		col2.markdown("### R\$ %.2f" % st.session_state['Cart'].total_price())