def automatic_code(cls: object) -> int:
    cls.code += 1
    new_code = cls.code
    return new_code

class Person:
    DNI_VALID_CHARS = "TRWAGMYFPDXBNJZSQVHLCKE"
    code = 0
    def __init__(self, dni:str,  name:str, surnames: str, address: str, phone: str, email: str, birth_date: str):
        self.code = automatic_code(Person)              # No
        self.dni = Person.check_dni(dni.upper())                 # No
        self.birth_date = birth_date   # No
        self.name = name
        self.surnames = surnames   
        self.address = address
        self.phone = phone
        self.email = email

    def name_change(self, new_name: str):
        self.name = new_name

    def surname_change(self, new_surname: str):
        self.surname = new_surname

    def address_change(self, new_address: str):
        self.address = new_address

    def phone_change(self, new_phone: str):
        self.phone = new_phone

    def email_change(self, new_email: str):
        self.email = new_email
    
    def __str__(self) -> str:
        return f"{self.name} with code: {self.code}"

    @staticmethod
    def check_dni(dni) -> str:
        if Person.DNI_VALID_CHARS[int(dni[:-1]) % 23] != dni[-1]:
            raise InvalidDNI(dni)
        return dni

class InvalidDNI(Exception):
    def __init__(self, dni):
        self.dni = dni

    def __str__(self) -> str:
        return f"{self.dni} is not a valid DNI"

class InvalidPrice(Exception):
    def __init__(self, price):
        self.price = price

    def __str__(self) -> str:
        return f"{self.price} is not a valid price"


class Administrador:
    def __init__(self, dni:str,  name:str, surnames: str, address: str, phone: str, email: str, birth_date: str):
        super().__init__(dni, name, surnames, address, phone, email, birth_date)

class Component:
    code = 0
    def __init__(self, price, type):
        self.code = automatic_code(Component)
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

class Product:
    def __init__(self, code, price):
        pass


pepe = Person("43389235B", "Pepe", "Gonzalez", "Calle 123", "145223589", "anpch@example.com", "1990-01-01")
pepe.name_change("julian")
print(pepe)
pepa = Component(7, "RAM")
print(pepa)
pep2 = Component(3, "Fuente de alimentacion")
print(pep2)
pepe2 = Person("4337245g", "Pepe", "Gonzalez", "Calle 123", "145223589", "anpch@example.com", "1990-01-01")
print(pepe2)
