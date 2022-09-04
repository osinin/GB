# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

while True:
    n_1 = int(input('Enter number: '))
    n_2 = int(input('Enter degree (without minus): '))
    if n_2 * (-1) < 0:
        break
    else:
        continue


def stepen(n_1, n_2):
    n = 1
    devisor = n_1
    while n <  n_2:
        devisor = devisor * n_1
        n += 1
        print(n, devisor)
    res = 1 / devisor
    return res


print(stepen(n_1, n_2))