"""
Семинар занятие №2
Дополнительные задания:
1)Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""
number = int(input("Введите число: "))
my_sum = 0
mult = 1

while number > 0:
    digit = number % 10
    my_sum = my_sum + digit
    mult = mult * digit
    number = number // 10

print("Сумма:", my_sum)
print("Произведение:", mult)
