# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

current_rating = [7, 5, 3, 3, 2]
user_num = int(input('Enter number from 1 to 9: '))
if user_num in current_rating:
    pos = current_rating.index(user_num)
    if pos != 0:
        current_rating.insert(pos, user_num)
    else:
        current_rating.insert(0, user_num)
else:
    if user_num > max(current_rating):
        current_rating.insert(0, user_num)
    elif user_num < min(current_rating):
        pos = len(current_rating)
        current_rating.insert(pos, user_num)
    else:
        for i in current_rating:
            if user_num > i:
                pos = current_rating.index(i)
                current_rating.insert(pos, user_num)
                break
            else:
                continue
print(current_rating)

