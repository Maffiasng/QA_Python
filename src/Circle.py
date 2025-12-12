from src.Figure import Figure


class Circle(Figure):
    def __init__(self, rad_r: int | float):
        if isinstance(rad_r,str):
            raise TypeError("Не хитри тут!!!")
        if rad_r <= 0 or not isinstance(rad_r,(int, float)):
            raise ValueError(f"Попробуй еще раз! Это похоже на радиус круга {rad_r} ?")
        self.rad_r = rad_r
        self._p = 3.14

    @property
    def area(self):
        return  2 * self._p * self.rad_r

    @property
    def perimeter(self):
        return self._p * (self.rad_r ** 2)

