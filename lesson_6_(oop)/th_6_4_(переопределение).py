class Transport:
    def show_info(self):
        print("Родительский метод класса Transport")


class Auto(Transport):
    def show_info(self):
        print("Дочерний метод класса Auto")
        # обращение к родительскому классу (2 варианта)
        super().show_info()
        Transport.show_info(self)

class Bus(Transport):
    def show_info(self):
        print("Дочерний метод класса Bus")


a = Auto()
a.show_info()

b = Bus()
b.show_info()