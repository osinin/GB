# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
user_list = list(input('Please input your nubers without spaces: '))

for i in range(1, len(user_list), 2):
    user_list.insert(i-1, user_list[i])
    user_list.pop(i + 1)
print(user_list)