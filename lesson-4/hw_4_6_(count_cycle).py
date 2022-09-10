"""
Реализовать два небольших скрипта:
● итератор, генерирующий целые числа, начиная с указанного;
● итератор, повторяющий элементы некоторого списка, определённого заранее.

Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import count, cycle


def counter(starter, stopper):
    try:
        for el in count(starter):
            if el > stopper:
                break
            else:
                print(el)
    except TypeError:
        print("Only Numbers!")


counter(3, 10)


my_list = ['ABC', 23, True]


def cycler(your_list, stopper):
    i = 0
    for el in cycle(my_list):
        if i > stopper:
            break
        else:
            print(el)
            i += 1


cycler(my_list, 10)