f = open("text_3.txt", "r", encoding="UTF-8")

content = f.read(10)
print(content.split("\n"))
print("- - - - - - - - - - -")

print(content)
print("- - - - - - - - - - -")

"чтение 1 строки"
content_2 = f.readline()
print(content_2)
print("- - - - - - - - - - -")

"чтение всех строк и вывод списком"
content_3 = f.readlines()
print(content_3)
print("- - - - - - - - - - -")

for i in content:
    print(i)

for i in content:
    print(i, end="")

"запись. выставить режим на запись"
f = open("text_3.txt", "a", encoding="UTF-8")
f.write('Осинин 100500\n')

f = open("text_3.txt", "r", encoding="UTF-8")
content = f.read()
print(content.split("\n"))
print("- - - - - - - - - - -")

f.close()


with open ("my_txt.txt", "x+", encoding="UTF-8") as food:
    food.writelines([f"watermelon\napple\n{1, 2, 3}\n"])
    food.seek(0)
    print(food.read())
