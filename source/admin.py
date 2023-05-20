from person import Person

class Administrador(Person):
    def __init__(self, dni:str, name:str, surnames: str, address: str, phone: str, email: str, birth_date: str):
        super().__init__(dni, name, surnames, address, phone, email, birth_date)