from src.rectangle import Rectangle
import pytest

@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
    pytest.param(3, 5, 16, id='integr_poz'),
    pytest.param(3.5,10.1,27.2, id='floter_poz'),
    pytest.param(1, 2, 16, id='integr_negative'),
    pytest.param(11, 0.5, 20.5, id='floter_negative')
    ]
)

def test_rectangle_positive_negative(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area  == area, f"Площадь не равна {area}, утебя {r.area}"

@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
    pytest.param(-1, 0, id='input zero'),
    pytest.param(3/5, 10/1, id='drobi')
    ]
)

def test_rectangle_negative(side_a,side_b):
    r = Rectangle(side_a,side_b)
    assert pytest.raises(ValueError, match='Как у прямоугольника ОДНА из сторон может быть меньше нуля?')

a = 2 #Если изменитьна 1 то скипнутый тест начнет запускаться.
#Почему skipif не отрабатывает, когда в тест переданы параментры из parametrize ?
@pytest.mark.skipif(condition=a == 2, reason="For test")
def test_rectangle_negative_for_skip():
    r = Rectangle(0, 12)
    assert pytest.raises(ValueError, match='Как у прямоугольника ОДНА из сторон может быть меньше нуля?')

