"""
Семинар занятие №1
Базовые задания
2)Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

n = int(input("Введите секунды: "))
sec = n % (24 * 3600)
hour = sec // 3600
sec %= 3600
minutes = sec // 60
sec %= 60
print(f"Ваше время {hour}:{minutes}:{sec}")
