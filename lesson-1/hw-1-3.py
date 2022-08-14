# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num = int(input('Please, enter number: '))
val_1 = str(num)
val_2 = val_1 + val_1
val_3 = val_2 + val_1
result = int(val_1) + int(val_2) + int(val_3)
print(f'Your sum is: {result}')