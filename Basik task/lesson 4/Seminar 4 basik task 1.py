"""
Семинар занятие №4
Базовые задания:
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script, hours, money_in_hour, bonus = argv


def calс_salary(hours_work, money_work_hour, bonus_work):
    try:
        result = (int(hours_work) * float(money_work_hour)) + float(bonus_work)
    except ValueError:
        return
    return result


print(f"{calс_salary(hours, money_in_hour, bonus)}")
