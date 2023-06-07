from auto_code import automatic_code
from errors import *


class Component:
    code = 0

    def __init__(self, price, type):
        self.code = automatic_code(Component)
        if price < 0:
            raise InvalidPrice(price)
        self.price = price
        self.type = type

    def __str__(self):
        return f"Product: {self.code}\nPrice: {self.price}\nType: {self.type}"

    def change_price(self, price):
        if price > 0:
            self.price = price
        return InvalidPrice(price)

    def change_type(self, type):
        self.type = type
