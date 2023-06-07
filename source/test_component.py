import pytest
import component


@pytest.fixture
def first_component():
    return component.Component(7, "RAM")


def test_create_component_with_wrong_price():
    price = -1

    with pytest.raises(component.InvalidPrice) as err:
        component.Component(-1, "Fuente de alimentacion")
    assert str(err.value) == f"{price} is not a valid price"


def test_str(first_component):
    assert (
        str(first_component)
        == f"Product: {first_component.code}\nPrice: {first_component.price}\nType: {first_component.type}"
    )


def test_change_price(first_component, new_price=10):
    first_component.change_price(new_price)
    assert first_component.price == new_price


def test_change_type(first_component, new_type="refrigeración"):
    first_component.change_type(new_type)
    assert first_component.type == new_type
