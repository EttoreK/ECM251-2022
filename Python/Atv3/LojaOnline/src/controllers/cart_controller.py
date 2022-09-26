import streamlit as st
from src.models.cart import Cart

class CartController():
	def __init__(self):
    # Carrega os dados dos usuários
		self.cart = Cart()
	def add_cart(self, prod):
		return self.adicionar(prod)
	