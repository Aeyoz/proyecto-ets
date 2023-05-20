from auto_code import automatic_code

class Product:
    code = 0
    def __init__(self, type):
        self.code = automatic_code(Product)
        self.price = type