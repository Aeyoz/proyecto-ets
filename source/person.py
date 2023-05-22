from auto_code import automatic_code
from errors import InvalidDNI


class Person:
    DNI_VALID_CHARS = "TRWAGMYFPDXBNJZSQVHLCKE"
    code = 0

    def __init__(
        self,
        dni: str,
        name: str,
        surnames: str,
        address: str,
        phone: str,
        email: str,
        birth_date: str,
    ):
        self.code = automatic_code(Person)
        self.dni = Person.check_dni(dni.upper())
        self.birth_date = birth_date
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


if __name__ == "__main__":
    pepe = Person(
        "43389235B",
        "Pepe",
        "Gonzalez",
        "Calle 123",
        "145223589",
        "anpch@example.com",
        "1990-01-01",
    )
    pepe.name_change("julian")
    print(pepe)
    pepe2 = Person(
        "4337245g",
        "Pepe",
        "Gonzalez",
        "Calle 123",
        "145223589",
        "anpch@example.com",
        "1990-01-01",
    )
    print(pepe2)
