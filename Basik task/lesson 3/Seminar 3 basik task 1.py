"""
Семинар занятие №3
Базовые задания
1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def dividing(a, b):
# Функция деления числа
    try:
        result = a / b
    except ZeroDivisionError:
    # Обработка ситуации деления на ноль
        return
    return result


try:
    n1 = float(input("a = "))
    n2 = float(input("b = "))
    print(f"a / b = {dividing(n1, n2)}")
except ValueError:
# Обработка ситуации ввода текстовых данных
    print("Incorrect input value")
