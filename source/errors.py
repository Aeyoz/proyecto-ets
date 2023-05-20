class InvalidDNI(Exception):
    def __init__(self, dni):
        self.dni = dni
        super().__init__(f"{self.dni} is not a valid DNI")

class InvalidPrice(Exception):
    def __init__(self, price):
        self.price = price
        super().__init__(f"{self.price} is not a valid price")

class InvalidProduct(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(f"{msg} already exists")