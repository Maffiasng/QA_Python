from src.triangle import Triangle
import pytest

@pytest.fixture
def get_tringle_date():
    side_c, side_a, side_b, area = 5, 10, 5, 34

    side_c += 1
    side_a += 4
    side_b += 5
    area = 20

    yield side_c, side_a, side_b, area

def test_tringle_positive(get_tringle_date):
    side_c, side_a, side_b, area = get_tringle_date
    r = Triangle(side_c, side_a, side_b)
    assert  r.area >= area, f"Неможет быть меньше, у тебя {r.area}"

@pytest.mark.skip(reason="For test")
def test_tringle_positive(get_tringle_date):
    side_c, side_a, side_b, area = get_tringle_date
    r = Triangle(side_c, side_a, side_b)
    assert  r.area <= area, f""