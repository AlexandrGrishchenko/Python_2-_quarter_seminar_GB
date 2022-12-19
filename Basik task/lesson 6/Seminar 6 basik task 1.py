"""
Семинар занятие №6
Базовые задания:
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать,
вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться
"""
from cProfile import run
from functools import reduce
from timeit import timeit

#Задача: нахождение максимального числа списка
list1 = [1, 4, 5, 2, 6]

#Это самая простая реализация, но она немного медленнее, поскольку мы используем этот алгоритм в цикле.
def large(arr):
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
            max_ = ele
    return max_

print(f"Алгоритм в цикле. {large(list1)}")
# Обработка алгоритма в цикле составило 0.35
print(timeit("large(list1)", globals=globals()))

# Использование встроенной функции reduse и max уменьшило время как написание самого кода так и время обработки вычисления
reduse_max = reduce(max, list1)
print(f"Встроенная функция reduse и max. {reduse_max}")
# Обработка через встроенную функцию составило 0.02
# Данный метод является более эффективным более чем в 13 раэ
print(timeit("reduse_max", globals=globals()))
def main():
    list1 = [1, 4, 5, 2, 6]
    my_cycle = large(list1)
    reduse_max = reduce(max, list1)

# Импортирование модуля run
run('main()')