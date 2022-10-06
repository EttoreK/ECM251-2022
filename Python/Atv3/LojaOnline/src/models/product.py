class Product():
    def __init__(self, name, price, img, desc):
        self._name = name
        self._price = price
        self._img = img
        self._desc = "Bom dia"

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_img(self):
        return self._img
    
    def get_desc(self):
        return self._desc