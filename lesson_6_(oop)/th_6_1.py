class MyAuto:
    # атрибуты класса (можно запрашивать в __init__)
    # name = "WV"
    # model = "Polo"
    # year = 2012
    a_count = 0

    # атрибуты объекта
    def __init__(self, n, m, y):
        self.name = n
        self.model = m
        self.year = y
        self.wheels = 4
        print(n, m, y)
        MyAuto.a_count +=1

    # Методы
    def on_start(self, speed):
        print(f"Lets Go car {self.name}! with speed {speed} "
              f"and {self.wheels} wheels")

    def on_stop(self):
        print(f'STOP model {self.model}!')


# auto_1 = MyAuto()
# auto_1.on_start()
# print(auto_1.name)
# auto_1.name = 'Lexus'
# print(auto_1.name)
#
# auto_2 = MyAuto()
# auto_2.on_start()
# print(auto_2.name)

auto_1 = MyAuto("VW", "Polo", "2012")
auto_1.on_start(100)
print(auto_1.a_count)
auto_2 = MyAuto("Lexus", "ES-250", "2019")
auto_2.on_start(120)
print(auto_2.a_count)
