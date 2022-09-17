class MyAuto:

    # атрибуты объекта
    def __init__(self, n, m, y):
        self.name = n
        self._model = m
        self.__year = y

    def on_start(self):
        print(f"Lets Go car {self.__year}!")

    def on_stop(self):
        print(f'STOP model {self._model}!')

    def get_year(self):
        return self.__year


auto_1 = MyAuto("VW", "Polo", "2012")
auto_1.on_start()
auto_1.on_stop()
print(auto_1._model)
print(auto_1.get_year())
print(auto_1._MyAuto__year)
print(auto_1.__year)