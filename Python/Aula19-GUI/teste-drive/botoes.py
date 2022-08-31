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
ttk.Button(
	base,
	text="ola mundo",
	bootstyle="default",
	command=acao_botao
).pack(side=LEFT, padx=10, pady=5)

#Ponto de entrada da interface
base.mainloop()