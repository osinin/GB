"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""
f = open("hw_5_2.txt", "r", encoding="UTF-8")
rows = f.readlines()
words = f.read()
print(f"В этом файле {len(rows)} строки, а количество слов - {words.count(' ') + len(rows)}")