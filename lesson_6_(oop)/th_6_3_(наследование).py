class Transport:
    # атрибуты объекта
    def __init__(self, n, m, y):
        self.name = n
        self.model = m
        self.year = y

    # Методы
    def on_start(self, speed):
        print(f"Lets Go car {self.name}! with speed {speed}")

    def on_stop(self):
        print(f'STOP model {self.model}!')


class MyAuto(Transport):
    #изменяем метод родительского класса:
    def __init__(self, n, m, y, p):
        super().__init__(n, n, y)
        self.passanger = p

    def drift(self):
        print(print(f"yoooo {self.model}"))


auto_1 = MyAuto("VW", "Polo", "2012", 4)
auto_1.on_start(100)
auto_1.drift()

auto_2 = MyAuto("Lexus", "ES-250", "2019", 5)
auto_2.on_start(120)
