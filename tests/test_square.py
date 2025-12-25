from src.square import Square
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

def test_square(rad_r):
    r = Square(rad_r)
    assert  r.perimeter >= 20, f"Давайте разбераться вместе!!"
