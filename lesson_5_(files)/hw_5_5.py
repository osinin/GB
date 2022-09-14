"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
from random import randint


sum = 0
orig_list = [randint(0, 1000) for _ in range(1, randint(2, 10))]
orig_str = ' '.join(str(i) for i in orig_list)
with open("hw_5_5.txt", "w+", encoding="UTF-8") as f:
    f.write(orig_str)
    f.seek(0)
    numbers = f.readline().split()
    print(numbers)
    for num in numbers:
        sum += int(num)
    print(sum)