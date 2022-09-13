"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""
rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("hw_5_4_new.txt", "w", encoding="UTF-8") as new_file:
    with open("hw_5_4.txt", "r", encoding="UTF-8") as f:
        new_file.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in f])