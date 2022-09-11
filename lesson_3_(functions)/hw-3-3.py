# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def sum_of_max(first, second, third):
    my_list = [first, second, third]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "Enter only numbers!"


print(sum_of_max(-50, 2, 3))

""" второй подход """

my_func = lambda first, second, third: (first + second + third) - min(first, second, third)
print(my_func(-5, 10, 12))
