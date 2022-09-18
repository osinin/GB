"""
2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _weight = 25
    _thickness = 0.05

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def mass_calc(self):
        return self._length * self._width * self._weight * self._thickness


work = Road(10000, 10)
res = work.mass_calc()
print(f"length is {work._length}")
print(f"width is {work._width}")
print(f"weight is {work._weight}")
print(f"thickness is {work._thickness}")
print(f"You need {res / 1000} tons")