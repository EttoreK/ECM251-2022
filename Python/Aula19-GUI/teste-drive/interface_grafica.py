import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MinhaUI():
	def acao_botao(self):
		print("Sim")

	def _construir_base(self):
		janela = ttk.Window(
			title="Minha GUI Mauá",
			size=(1024,400),
			position=(100,100),
			minsize=(600,300),
			maxsize=(2400,1200),
			alpha=1,
			iconphoto="calc_ic.png"
		)
		return janela

	def __init__(self) -> None:
		self.base = self._construir_base()

		#criando um botão
		bot1 = ttk.Button(
			self.base,
			text="Olá Mundo",
			bootstyle="default",
			command=self.ativa_bot
		).pack(side=LEFT, padx=10, pady=5)

		#criando botão 2
		self.bot2 = ttk.Button(
			self.base,
			text="2º Botão",
			bootstyle=(DANGER, OUTLINE),
			command=self.desativa_bot
		)
		
		self.bot2.pack(side=LEFT, padx=10, pady=5)
	
	def run(self):
		self.base.mainloop()
	
	def ativa_bot(self):
		print("Ligando Botão")
		self.bot2.configure(state="enable")
	def desativa_bot(self):
		print("Desligando Botão")
		self.bot2.configure(state="disabled")

if __name__ == "__main__":
	app = MinhaUI()
	app.run()