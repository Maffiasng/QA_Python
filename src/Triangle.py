from src.Figure import Figure

class Triangle(Figure):
     def __init__(self, side_c: int | float,side_a: int | float,side_b: int | float):
         if side_c <= 0 or side_b <= 0:
             raise ValueError("Никаких нулей и мииносовых значений!")
         if side_c + side_b == side_a or side_a + side_b == side_c:
             raise ValueError("Увы!!! Не пытайся создать!Сума двух сторон не должна бытьровна третей стороне.")
         self.side_c = side_c
         self.side_a = side_a
         self.side_b = side_b

     @property
     def area(self):
         x = (self.side_a + self.side_b + self.side_c) / 2
         s = x * ((x - self.side_a) * (x - self.side_b) * (x - self.side_c))
         return s ** 0.5

     @property
     def perimeter(self):
         return self.side_a + self.side_b + self.side_c

