from cgitb import text
from email.mime import base
from sre_constants import JUMP
from tkinter.ttk import Style
from turtle import color
from unittest.mock import DEFAULT
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MinhaUI():
    def _construir_base(self):
        janela = ttk.Window(
            title="Loja Games Games",
            size= (1024,400),
            position= (100,100),
            minsize= (600,300),
            maxsize= (1800,900),
            alpha=1.0,
            themename='superhero',
            iconphoto='games.png'
        )
        return janela

    def _criar_texto(self, txt):
        return ttk.Entry(
            self.base,
            textvariable=txt,
        )
    
    def _entrar_usuario(self, usuario):
        usuario = self._criar_texto(usuario)
        return usuario

    def _entrar_senha(self, senha):
        senha = self._criar_texto(senha)
        return senha


    # # store email address and password
    # email = "34"
    # password = "3434"

    # def login_clicked(email, password):
    #     """ callback when the login button clicked
    #     """
    #     msg = f'You entered email: {email} and password: {password}'
    #     # showinfo(
    #     #     title='Information',
    #     #     message=msg
    #     # )

    #     # Sign in frame
    #     signin = ttk.Frame(base)
    #     signin.pack(padx=10, pady=10, fill='x', expand=True)


    #     # email
    #     email_label = ttk.Label(signin, text="Email Address:")
    #     email_label.pack(fill='x', expand=True)

    #     email_entry = ttk.Entry(signin, textvariable=email)
    #     email_entry.pack(fill='x', expand=True)
    #     email_entry.focus()

    #     # password
    #     password_label = ttk.Label(signin, text="Password:")
    #     password_label.pack(fill='x', expand=True)

    #     password_entry = ttk.Entry(signin, textvariable=password, show="*")
    #     password_entry.pack(fill='x', expand=True)

    #     # login button
    #     # login_button = ttk.Button(signin, text="Login", command=login_clicked)
    #     # login_button.pack(fill='x', expand=True, pady=10)

    def _criar_botao(self, texto, acao):
        return ttk.Button(
            self.base,
            text=texto,
            bootstyle=(DEFAULT),
            command=acao
        )

    def __init__(self) -> None:
        self.base = self._construir_base()
        self.bot = self._criar_botao(texto="AÇÃO", acao=self.mostrar_texto)
        self.bot.grid(row=3, column=2, padx=5, pady=5)
        self.valor_digitado = ""
        # self.text = self._criar_texto(usuario=self.valor_digitado)
        # self.text = self.login_clicked( password="123")
        self.usuario = self._entrar_usuario(usuario='')
        self.usuario.grid(row=2, column=1, padx=5, pady=5)
    
    def run(self):
        self.base.mainloop()

    def mostrar_texto(self):
        user = self.usuario.get()
        with open('usuarios.txt') as f:
            lines = f.readlines()
        for a in lines:
            print(user)
            print(a)
            if (a=='\n'):
                break
            elif (a == user):
                print("Entrou: ", user)
                break
            elif (a == ''):
                print("Falha: ")
                break
        


if __name__ == "__main__":
    app = MinhaUI()
    app.run()