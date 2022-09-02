# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
while True:
    mm = int(input('Enter number from 1 to 12: '))
    if mm > 0 and mm <= 12:
        print(month_list[mm - 1])
        break
    else:
        continue
