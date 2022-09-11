# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

user_name = input('Enter your name: ')
user_city = input('Enter your city: ')
user_age = int(input('Enter your year of birth: '))


def user_info(name, city, age):
    print(f"Your name is {user_name}, you are from {user_city} and you was born in {user_age}")


user_info(age=user_age, name=user_name, city=user_city)
