"""
1. Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class Lighter:

    def __init__(self, col, t):
        self.__color = col
        self.__timer = t

    def show_col(self):
        return self.__color

    def running(self):
        print(self.__color)
        time.sleep(self.__timer)


r = Lighter("Red", 5)
y = Lighter("Yellow", 2)
g = Lighter("Green", 5)

print(r.running())
print(y.running())
print(g.running())

