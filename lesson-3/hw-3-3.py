# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

users_first = int(input('Enter first number: '))
users_second = int(input('Enter second number: '))
users_third = int(input('Enter third number: '))


def sum_of_max(first, second, third):
    if first <= second and first <= third:
        return second + third
    elif first <= second and first >= third:
        return first + second
    else:
        return first + third


print(sum_of_max(users_first, users_second, users_third))
