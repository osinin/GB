# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
try:
    num = int(input('Please, enter number: '))
    num_len = len(str(num))
    maximum = 0
    if num >= 0:
        while num_len != 0:
            i = num % 10
            if i > maximum:
                maximum = i
                num = num // 10
                num_len = num_len - 1
            else:
                num = num // 10
                num_len = num_len - 1
        print(maximum)
    else:
        print('Number must be >=0')
except:
    print('Not a number')
