# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
while True:
    txt = input('Enter your word from small letter: ')
    if txt.islower() and txt.isascii() and not txt.isascii():
        break
    else:
        continue


def text_func(txt):
    new_txt = txt.title()
    return new_txt


print(text_func(txt))