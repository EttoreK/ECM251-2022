from sistema import Sistema
import streamlit as st
from src.controllers.cart_controller import CarrController
from src.controllers.item_controller import ItemController
from src.controllers.user_controller import UserController

# with open("./css/style.css") as f:
# 	st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

stm = Sistema()
ItemC = ItemController()
CarrC = CarrController()
UserC = UserController()
st.set_page_config(page_title="", page_icon="")

if "Cadastro" not in st.session_state:
	st.session_state["Cadastro"] = False

if "Login" not in st.session_state:
	st.session_state["Login"] = "negado"
	st.session_state["Usuario"] = ""
	st.session_state["email"] = ""
	st.session_state["Carr"] = CarrC

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
		prdct = ItemC.pegar_item('SQL')
		c = st.container()
		c.button(label = "Adicionar", key = stm.get_key(), on_click = CarrController.add_prod, args = (st.session_state['Carr'],prdct))

	col1, col2, col3 = st.columns(3,gap="large")
	
	with col1:
		prdct = ItemC.pegar_item('BDE')
		c = st.container()
		c.markdown("###### Yu-Gi-Oh! Duel Monsters")
		c.image("imgs/ygo.jpg", width=200)
		c.markdown("\r#### R$ 40,00")
		c.markdown("#### 224 episódios para assistir")
		c.button(label = "Adicionar", key = stm.get_key(), on_click = CarrController.add_prod, args = (st.session_state['Carr'],prdct))
			
	with col2:
		prdct = ItemC.pegar_item('ABC')
		c = st.container()
		c.markdown("###### My hero Academia")
		c.image("imgs/mha.jpg", width=200)
		c.markdown("\r#### R$ 120,00")
		c.markdown("#### 113 episódios para assistir")
		c.button(label = "Adicionar", key = stm.get_key(), on_click = CarrController.add_prod, args = (st.session_state['Carr'],prdct))

	with col3:
		prdct = ItemC.pegar_item('CAF')
		c = st.container()
		c.markdown("###### Digimon")
		c.image("imgs/dgm.jpg", width=200)
		c.markdown("\r\n#### R$ 9,00")
		c.markdown("#### Vários episódios para assistir")
		c.button(label = "Adicionar", key = stm.get_key(), on_click = CarrController.add_prod, args = (st.session_state['Carr'],prdct))
	
with tab2:
	if "Login" not in st.session_state:
		st.session_state["Login"] = "negado"
		st.session_state["Usuario"] = ""
		st.session_state["email"] = ""

	if st.session_state["Login"] != "aprovado":
		st.header("Login")
		user = st.text_input(
			label="user",
			placeholder="Usuário",
			label_visibility= "hidden"
		)
		password = st.text_input(
			label="senha",
			placeholder="Senha",
			type = "password",
			label_visibility= "hidden"
		)
		
		if not st.session_state["Cadastro"]:
			col1, col2 = st.columns(2)
			with col1:
				st.button(label= "Entrar", key = stm.get_key(), on_click= UserController.check_login, args = (UserC,user,password))
			with col2:
				st.button(label= "Cadastrar", key = stm.get_key(), on_click= stm.inverte, args= ())
		else:
			password2 = st.text_input(
				label="pass2",
				label_visibility="hidden",
				placeholder="Confirmar senha",
				type = "password"
			)
			email = st.text_input(
				label="email",
				label_visibility="hidden",
				placeholder="Email"
			)
			st.button(label= "Criar conta", key = stm.get_key(), on_click= UserController.cadastrar, args = (UserC,user,password,password2,email))
			st.markdown("Erro")
	else:
		st.header("Perfil")

		col1, col2 = st.columns(2)

		with col1:
			st.image(image="imgs/us.jpg", width=350)
			
		with col2:
			st.markdown(f"### Nome:\n{st.session_state['Usuario']}")
			st.markdown(f"### Email:\n{st.session_state['email']}")
		
		st.button(label= "Sair", key = stm.get_key(), on_click= UserController.logout, args=(UserC, st.session_state['Carr']))

with tab3:
	if 'Carr' in st.session_state:

		row = st.container()
		col1,col2,col3 = st.columns(3)
		col1.markdown("##### Produto")
		col2.markdown("##### Preço")
		col3.markdown("##### Excluir\n\n\n")
		prods = st.session_state['Carr'].get_prod()
		if prods != None:
			with row:
				for i in prods:
					col1.markdown("#### %s" % i.get_name())
					col2.markdown("#### R\$ %.2f" % i.get_price())
					col3.button(label= "Remover", key = stm.get_key() , on_click=CarrController.tira_prod , args=(st.session_state['Carr'],i.get_name()))

		col1, col2 = st.columns(2)

		col1.markdown("### Preço Total:")
		col2.markdown("### R\$ %.2f" % st.session_state['Carr'].ttl_cust())
