import streamlit as st
from sistema import Sistema

stm = Sistema()
stm.comeco()

# with open("./css/style.css") as f:
# 	st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
# st.set_page_config(page_title="", page_icon="")

tab1, tab2, tab3 = st.tabs(["Início", "Perfil", "Carrinho"])

with tab1:
	# Titulo
	st.header("Início")

	if stm.verifica_adm():
		c_exp = st.expander("Adicionar Produto", expanded=False)
		c_exp.header("Adicionar Produto")
		prod_id = c_exp.text_input(
			label="Id",
			placeholder="Id específico?",
			value = "",
			label_visibility= "hidden"
		)
		nome = c_exp.text_input(
			label="Nome",
			placeholder="Nome do produto",
			label_visibility= "hidden"
		)
		preco = c_exp.number_input(
			label="Preco",
			label_visibility= "hidden",
			value = 0.00
		)
		c_exp.button(label = "Adicionar produto", key = stm.get_key(), on_click = Sistema.add_produto_db, args = (stm, prod_id, nome, preco))

	# mostruario
	st.markdown("###### Pókemon")
	st.image(image = "imgs/pkm.jpg", width=700)
	col1, col2, col3 = st.columns(3,gap="large")
	with col1: 
		st.markdown("#### R$ 400,00")
	with col2:
		st.markdown("#### mais de 1000 episódios para assistir")
	with col3:
		prdct = stm.pega_item("PKM")
		c = st.container()
		c.button(label = "Adicionar", key = stm.get_key(), on_click = stm.add_produto_carr, args = (st.session_state['Carr'], prdct))

	col1, col2, col3 = st.columns(3,gap="large")
	
	with col1:
		prdct = stm.pega_item("YGO")
		c = st.container()
		c.markdown("###### Yu-Gi-Oh! Duel Monsters")
		c.image("imgs/ygo.jpg", width=200)
		c.markdown("\r#### R$ 40,00")
		c.markdown("#### 224 episódios para assistir")
		c.button(label = "Adicionar", key = stm.get_key(), on_click = stm.add_produto_carr, args = (st.session_state['Carr'], prdct))
			
	with col2:
		prdct = stm.pega_item("BNH")
		c = st.container()
		c.markdown("###### My hero Academia")
		c.image("imgs/mha.jpg", width=200)
		c.markdown("\r#### R$ 120,00")
		c.markdown("#### 113 episódios para assistir")
		c.button(label = "Adicionar", key = stm.get_key(), on_click = stm.add_produto_carr, args = (st.session_state['Carr'], prdct))

	with col3:
		prdct = stm.pega_item("DGM")
		c = st.container()
		c.markdown("###### Digimon")
		c.image("imgs/dgm.jpg", width=200)
		c.markdown("\r\n#### R$ 9,00")
		c.markdown("#### Vários episódios para assistir")
		c.button(label = "Adicionar", key = stm.get_key(), on_click = stm.add_produto_carr, args = (st.session_state['Carr'], prdct))
	
with tab2:
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
				st.button(label= "Entrar", key = stm.get_key(), on_click= Sistema.verifica_login, args = (stm,user,password))
			with col2:
				st.button(label= "Cadastrar", key = stm.get_key(), on_click= stm.inverte_estado_cadastro)
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

			st.button(label= "Criar conta", key = stm.get_key(), on_click= Sistema.realiza_cadastro, args = (stm,user,password,password2,email))
			if st.session_state["Estado_Cadastro"] == "Senha_Dispar":
				st.error("As senhas devem ser iguais")
			elif st.session_state["Estado_Cadastro"] == "Senha_Vaz":
				st.error("Preenha todos os campos (\"Nome\", \"Senha\", \"Confirmar senha\" e \"Email\")")
			elif st.session_state["Estado_Cadastro"] == "Email_Ig":
				st.error("Esse email já foi cadastrado")
			elif st.session_state["Estado_Cadastro"] == "Concluido":
				stm.verifica_login(user, password)
	else:
		st.header("Perfil")

		col1, col2 = st.columns(2)

		with col1:
			st.image(image="imgs/us.jpg", width=350)
			
		with col2:
			st.markdown(f"### Nome:\n{st.session_state['Usuario']}")
			st.markdown(f"### Email:\n{st.session_state['Email']}")
		
		c_exp = st.expander("Alterar dados", expanded=False)
		c_exp.header("Preencha para alterar os dados")
		nome_usu = c_exp.text_input(
			label="Novo nome",
			placeholder="Novo nome",
			label_visibility= "hidden"
		)
		email_usu = c_exp.text_input(
			label="Novo email",
			placeholder="Novo email",
			label_visibility= "hidden"
		)
		senha_usu = c_exp.text_input(
			label="Nova senha",
			placeholder="Nova senha",
			label_visibility= "hidden"
		)
		senha_usu2 = c_exp.text_input(
			label="Nova senha",
			placeholder="confirmar nova senha",
			label_visibility= "hidden"
		)

		c_exp.button(label = "Aplicar alteracoes", key = stm.get_key(), on_click = Sistema.altera_usuario, args = (stm, nome_usu, email_usu, senha_usu, senha_usu2))
		st.button(label= "Sair", key = stm.get_key(), on_click= stm.sair)

with tab3:
	if 'Carr' in st.session_state:

		row = st.container()
		col1,col2,col3 = st.columns(3)
		col1.markdown("##### Produto")
		col2.markdown("##### Preço")
		col3.markdown("##### Excluir\n\n\n")
		prods = stm.pega_produtos_carrinho()
		if prods != None:
			with row:
				for item in prods:
					col1.markdown("#### %s" % stm.pega_prod_nome(item))
					col2.markdown("#### R\$ %.2f" % stm.pega_prod_preco(item))
					col3.button(label= "Remover", key = stm.get_key() , on_click= stm.remove_produto_carrinho , args=(st.session_state['Carr'], item))

		col1, col2 = st.columns(2)
		col1.markdown("### Preço Total:")
		col2.markdown("### R\$ %.2f" % stm.preco_total())