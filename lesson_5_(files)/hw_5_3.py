"""
3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
"""
f = open("hw_5_3.txt", "r", encoding="UTF-8")
rows = f.readlines()
sum = 0
for row in rows:
    try:
        sum += float(row.split()[1])
        if float(row.split()[1]) < 20000:
            print(row.split()[0])
    except ValueError:
        continue
print(f'avg salary is {sum / len(rows)}')
