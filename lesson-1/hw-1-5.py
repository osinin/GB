# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

profit = int(input('Please, enter profit: '))
loss = int(input('Please, enter loss: '))

if profit > loss:
    print('PROFIT!')
    rent = (profit - loss) / profit
    emp = int(input('Please, enter number of employees: '))
    emp_prof = profit / emp
    print(f'rent is {rent} and employee profit is {emp_prof}')
elif profit == loss:
    print('NO PROFIT!')
else:
    print('LOSS!')
