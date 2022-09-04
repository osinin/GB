# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(divident, devisor):
    try:
        quotient = divident / devisor
        return quotient
    except ZeroDivisionError:
        print("Devision by Zero!")


divident = int(input('Enter divident: '))
devisor = int(input('Enter devisor: '))
print(division(divident, devisor))
