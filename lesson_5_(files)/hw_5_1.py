"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
f = open("hw_5_1.txt", "w", encoding="UTF-8")
inp = input('Enter your text: ')
f.write(f'{inp}\n')
f.close()
f = open("hw_5_1.txt", "a", encoding="UTF-8")
while True:
    inp = input('Press Q for exit or continue adding text: ')
    if inp.lower() == "q" or inp == '':
        f.close()
        print('Exited')
        break
    else:
        f.write(f'{inp}\n')
        print('text added')
f.close()