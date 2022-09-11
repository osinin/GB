# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров
# a и b и выводить одно натуральное число — номер дня.

while True:
    res_a = float(input('Please, enter first day result: '))
    res_b = float(input('Please, enter goal result: '))
    i = 1
    current_result = res_a
    if res_a <=0 or res_b < 0:
        print('res_a and res_b must be >0')
    else:
        while current_result < res_b:
            i = i + 1
            current_result = current_result * 1.1
        print(i)
        break
