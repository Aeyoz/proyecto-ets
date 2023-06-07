import pytest
import person


@pytest.fixture
def first_person():
    return person.Person(
        "43389235B",
        "Ayoze",
        "Hernández Díaz",
        "Bajo un puente",
        "638343900",
        "elpayov2@gmail.com",
        "20/09/2002",
    )


@pytest.fixture
def second_person():
    return person.Person(
        "43382832W",
        "Marlon",
        "Farizo Hergueta",
        "Bajo un puente",
        "638343900",
        "marlon@marlon.marlon",
        "20/09/2002",
    )


def test_create_person_with_wrong_dni():
    dni = "43389235X"

    with pytest.raises(person.InvalidDNI) as err:
        person.Person(
            "43389235X",
            "Marlon",
            "Farizo Hergueta",
            "Bajo un puente",
            "638343900",
            "marlon@marlon.marlon",
            "20/09/2002",
        )
    assert str(err.value) == f"{dni} is not a valid DNI"


def test_change_name(second_person, new_name="pepe"):
    second_person.name_change(new_name)
    assert second_person.name == new_name


def test_change_surname(first_person, new_surname="Alonso"):
    first_person.surname_change(new_surname)
    assert first_person.surname == new_surname


def test_change_address(second_person, address="Calle vieja pero nueva"):
    second_person.address_change(address)
    assert second_person.address == address


def test_change_email(first_person, email="elpayo56@gmail.com"):
    first_person.email_change(email)
    assert first_person.email == email


def test_str(first_person):
    assert str(first_person) == f"{first_person.name} with code: {first_person.code}"


def test_atributes():
    dni = "43382832W"
    name = "Marlon"
    surnames = "Farizo Hergueta"
    address = "Bajo un puente"
    phone_number = "638343900"
    mail = "marlon@marlon.marlon"
    birth_date = "20/09/2002"
    new_person = person.Person(
        "43382832W",
        "Marlon",
        "Farizo Hergueta",
        "Bajo un puente",
        "638343900",
        "marlon@marlon.marlon",
        "20/09/2002",
    )
    assert new_person.dni == dni
    assert new_person.name == name
    assert new_person.surnames == surnames
    assert new_person.address == address
    assert new_person.phone == phone_number
    assert new_person.email == mail
    assert new_person.birth_date == birth_date
