my_list = [2, 4, 6]
new_list = [el+10 for el in my_list]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

my_dict = {el: el * 2 for el in range(10, 15)}
print(my_dict)

my_set = {el ** 3 for el in range(5, 10)}
print(my_set)