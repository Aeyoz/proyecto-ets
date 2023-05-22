from auto_code import automatic_code
import person


class Product:
    code = 0

    def __init__(self, destination):
        self.code = automatic_code(Product)
        self.destination = destination


class BuyDetail:
    def __init__(self, code, time):
        self.code = f"{code}{self.time}"
        self.time = time

    def __str__(self):
        return f"{self.code}\n{self.time}"


"""def compra(item, qty, client):
    storage[item] = storage.get(item) - qty
    return BuyDetail(client.code, date)"""
