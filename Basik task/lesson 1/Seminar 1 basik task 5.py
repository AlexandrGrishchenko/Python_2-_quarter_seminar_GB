"""
Семинар занятие №1
Базовые задания
5)Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

profit = int(input("Введите значение прибыли: "))
expenses = int(input("Введите значение издержек: "))
people = int(input("Введите количество работников: "))
if profit > expenses:
    revenue = profit - expenses
    print(f"Выручка больше издержек и составила: {revenue}")
    rent = revenue / profit
    print(f"Рентабильность фирмы составила: {rent}")
    revenue_for_person = revenue / people
    print(f"Прибыль фирмы в расчете на одного сотрудника: {revenue_for_person}")
elif profit == expenses:
    print("Прибыль и издержки равны")
else:
    print("Фирма работает в убыток")
