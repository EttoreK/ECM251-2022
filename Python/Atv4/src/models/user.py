class User():
    def __init__(self, id_usu, name, email, password):
        self._id = id_usu
        self._name = name
        self._email = email
        self._password = password
    
    def get_password(self) -> str:
        return self._password

    def get_name(self) -> str:
        return self._name   

    def get_email(self) -> str:
        return self._email
    
    def get_id(self) -> str:
        return self._id

    def set_password(self, password):
        self._password = password
        
    def set_name(self, name) -> None:
        self._name = name

    def __str__(self) -> str:
        return f'User(id: {self._id}, name:{self._name}, email:{self._email}, password:{self._password})'