# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num = input('Please, enter number: ')
val_2 = num + num
val_3 = val_2 + num
result = int(num) + int(val_2) + int(val_3)
print(f'Your sum is: {result}')