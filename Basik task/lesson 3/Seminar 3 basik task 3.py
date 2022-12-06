"""
Семинар занятие №3
Базовые задания
3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    # Функция нахождения суммы наибольших двух аргументов из трех
    if (a + b) > (a + c) and (a + b) > (b + c):
        return a + b
    if (a + c) > (a + b) and (a + c) > (b + c):
        return a + c
    if (b + c) > (a + b) and (b + c) > (a + c):
        return b + c


try:
    n1 = int(input("a = "))
    n2 = int(input("b = "))
    n3 = int(input("c = "))
    print(f"Cумма наибольших двух чисел:  {my_func(n1, n2, n3)}")
except ValueError as e:
    print(f"{e}")
