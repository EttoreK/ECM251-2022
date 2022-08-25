from datetime import datetime


from datetime import date

class Perfil:
    def __init__(self, nome, telefone, foto = ""):
        self._nome = nome
        self._foto = foto
        self._dat_nasc = date.today()
        self._descricao = "BláBlóBlú"
        self._telefone = telefone