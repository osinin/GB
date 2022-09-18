"""
Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} класса Pen")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} класса Pencil")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} класса Handle")


item_0 = Stationery()
item_0.draw()

item_1 = Pen("simple_pen")
item_1.draw()

item_2 = Pencil("simple_pencil")
item_2.draw()

item_3 = Handle("simple_handle")
item_3.draw()