class Person:
    DNI_VALID_CHARS = "TRWAGMYFPDXBNJZSQVHLCKE"
    code = 0
    def __init__(self, dni:str,  name:str, surnames: str, address: str, phone: str, email: str, birth_date: str):
        self.code = Person.automatic_code()              # No
        self.dni = Person.check_dni(dni.upper())                 # No
        self.birth_date = birth_date   # No
        self.name = name
        self.surnames = surnames   
        self.address = address
        self.phone = phone
        self.email = email

    def name_change(self, new_name):
        self.name = new_name

    def surname_change(self, new_surname):
        self.surname = new_surname

    def address_change(self, new_address):
        self.address = new_address

    def phone_change(self, new_phone):
        self.phone = new_phone

    def email_change(self, new_email):
        self.email = new_email
    
    def __str__(self):
        return f"{self.name} with code: {self.code}"

    @staticmethod
    def automatic_code():
        Person.code += 1
        new_code = Person.code
        return new_code

    @staticmethod
    def check_dni(DNI):
        def wrapper(self):
            if Person.DNI_VALID_CHARS[self.dni % 23] != self.dni[-1]:
                raise InvalidDNI(DNI)
            return DNI
        return wrapper

class InvalidDNI(Exception):
    def __str__(self, message = "Invalid DNI"):
        super().__message__ = message

    def __str__(self):
        return f"{self.dni} -> {self.message}"
    

class Administrador:
    def __init__(self, dni:str,  name:str, surnames: str, address: str, phone: str, email: str, birth_date: str):
        super().__init__(dni, name, surnames, address, phone, email, birth_date)
    

pepe = Person("43389235T", "Pepe", "Gonzalez", "Calle 123", "145223589", "anpch@example.com", "1990-01-01")
pepe.name_change("julian")
print(pepe)
pepe2 = Person("4337245g", "Pepe", "Gonzalez", "Calle 123", "145223589", "anpch@example.com", "1990-01-01")
print(pepe2)
