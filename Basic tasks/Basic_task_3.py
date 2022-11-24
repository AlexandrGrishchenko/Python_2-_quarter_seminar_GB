"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = int(input("Введите число: "))
temp = str(n)
second_temp = temp + temp
third_temp = temp + temp + temp
result = n + int(second_temp) + int(third_temp)
print(f"{temp} + {temp + temp} + {temp + temp + temp} = {result}")

