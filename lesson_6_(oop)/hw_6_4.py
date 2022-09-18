"""
Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам,выведите результат.
Вызовите методы и покажите результат.
"""
class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name} started ride")

    def stop(self):
        print(f"Car {self.name} stopped")

    def turn(self, dir):
        print(f"Car {self.name} turned {dir}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        return "Speed limit warning" if self.speed > 60 else super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return "Speed limit warning" if self.speed > 40 else super().show_speed()


class PoliceCar(Car):
    pass


car_1 = TownCar("Polo", 80, "White")
print(car_1.show_speed())
car_1.turn("left")

car_2 = TownCar("KAMAZ", 40, "Blue")
print(car_2.show_speed())
car_2.turn("right")