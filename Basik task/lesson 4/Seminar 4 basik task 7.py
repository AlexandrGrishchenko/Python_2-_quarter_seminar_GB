"""
Семинар занятие №4
Базовые задания:
7) Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce

user_number = int(input("Enter number factorial: "))

# Решение задачи через range, reduce и lambda
lst = [el for el in range(1, user_number+1)]
# Reduce принимает функцию и возвращает произведение всех элементов списка
print(f"Factorial !{user_number} = {reduce(lambda a, x: a * x, lst)}")


# Функция подсчета интеграла с помощью yield
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

# Вывод интеграла каждого числа
i=1
for el in fact(user_number):
    i+=1
    print(f"!{i}={el}")