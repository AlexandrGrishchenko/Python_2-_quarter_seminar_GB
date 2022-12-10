"""
Семинар занятие №4
Базовые задания:
6) Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, islice, cycle
from sys import argv

lst = []

# # Данные для проверки
# fist_number = 2
# second_number = 6

# Решение через функцию вывода последовательности чисел range
def list_range(number_start, number_finish):
    print(f"Итератор range: {list(range(number_start, number_finish + 1))}")

# Решение через традиционный итератор islice
for i in islice(count(fist_number), second_number - 1):
    lst.append(i)
print(f"Итератор islice: {lst}")

# Решение через традиционный итератор count
for x in count(fist_number):
    if x > second_number:
        break
    lst.append(x)
print(f"Итератор count: {lst}")

# Решение через традиционный итератор cycle
count = fist_number
for item in cycle(lst):
    if count > second_number:
        break
    lst.append(item)
    count += 1
print(f"Итератор cycle: {lst}")

# Скрипт ввода чисел через терминал
try:
    Seminar 4 basik task 6, fist_number, second_number = argv
except  ValueError:
    fist_number = second_number = None

# Вывод списка в терминале
list_range(int(fist_number), int(second_number))
