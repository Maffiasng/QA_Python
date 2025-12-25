from src.circle import Circle
import pytest

@pytest.mark.parametrize(
    "rad_r",
    [
        pytest.param(50, id = "Valid"),
        pytest.param(10, id = "Valid"),
        pytest.param(0, id = "Not Valid"),
        pytest.param("10.6", id = "input Str")
    ]
)

def test_circle(rad_r):
    r = Circle(rad_r)
    assert  r.perimeter >= 20, f"Не спишите унас площадь круга должна строго ровна или мене 20"

def test_add_area():
    a = Circle(5)
    assert a.add_area(a), f"Что то пошло не поплану!"