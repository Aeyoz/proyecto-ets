import pytest
import person

@pytest.fixture
def first_person():
    return Person("43389235B", "Ayoze", "Hernández Díaz", "Bajo un puente", "638343900", "elpayov2@gmail.com", "20/09/2002")

def second_person():
    return Person("43382832W", "Marlon", "Farizo Hergueta", "Bajo un puente", "638343900", "marlon@marlon.marlon", "20/09/2002")



def test_change_name(new_name):
    assert 
    pe

def test_change_surname(first_person, new_surname):
    first_person.surname_change(new_surname)
    assert first_person.surname == new_surname

def test_change_address(second_person, address="Calle vieja pero nueva"):
    second_person.address_change(address)
    assert second_person.address == address

def test_change_email(first_person, email="elpayo56@gmail.com"):
    first_person.email_change(email)
    assert first_person.email == email

def test_str(first_person):
    assert f"{first_person.name} with code: {first_person.code}"

'https://prod.liveshare.vsengsaas.visualstudio.com/join?784E86228A925A29B49D9849B57053403073'
