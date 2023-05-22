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


class Refrigeration(Component):
    def __init__(self, price, type):
        super().__init__(price, type)


class RAM(Component):
    def __init__(self, price, type):
        super().__init__(price, type)


class Fuente(Component):
    def __init__(self, price, type):
        super().__init__(price, type)


class Motherboard(Component):
    def __init__(self, price, type):
        super().__init__(price, type)


class GPU(Component):
    def __init__(self, price, type):
        super().__init__(price, type)


class CPU(Component):
    def __init__(self, price, type):
        super().__init__(price, type)


class Case(Component):
    def __init__(self, price, type):
        super().__init__(price, type)


class Storage(Component):
    def __init__(self, price, type):
        super().__init__(price, type)


class Periferals(Component):
    def __init__(self, price, type):
        super().__init__(price, type)


pepa = Component(7, "RAM")
print(pepa)
pep2 = Component(3, "Fuente de alimentacion")
print(pep2)
