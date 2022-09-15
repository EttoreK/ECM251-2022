from models.user import User
import streamlit as st

class UserController():
    def login(user, password):
        d = {}
        with open("src/userdb.txt") as f:
            for line in f:
                (key, val) = line.split()
                d[key] = val
                User(name = key, password = val, email = None)
        try:
            if d[user] == password:
                return "L"
                print("logado")
            else:
                return "S"
                print("senha incorreta!")
        except KeyError:
            return "U"
            print("Usuario incorreto")