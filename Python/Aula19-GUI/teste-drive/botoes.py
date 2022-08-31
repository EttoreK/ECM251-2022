import ttkbootstrap as ttk
from ttkbootstrap.constants import *

base = ttk.Window(
	title="Minha GUI Mauá",
	size=(1024,400),
	position=(100,100),
	minsize=(600,300),
	maxsize=(2400,1200),
	alpha=1,
	iconphoto="calc_ic.png"
)

def acao_botao():
	print("Click!")

#criando um botão
bot1 = ttk.Button(
	base,
	text="Olá Mundo",
	bootstyle="default",
	command=acao_botao
).pack(side=LEFT, padx=10, pady=5)

#criando botão 2
bot2 = ttk.Button(
	base,
	text="2º Botão",
	bootstyle=(DANGER, OUTLINE),
	command=acao_botao
).pack(side=LEFT, padx=10, pady=5)

#Ponto de entrada da interface
base.mainloop()