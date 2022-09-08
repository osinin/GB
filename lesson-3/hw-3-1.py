# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(divident, devisor):
    try:
        quotient = int(divident) / int(devisor)
        return quotient
    except ZeroDivisionError:
        return "Devision by Zero!"
    except ValueError:
        return "Value Error!"


divident = input('Enter divident: ')
devisor = input('Enter devisor: ')
print(division(divident, devisor))
