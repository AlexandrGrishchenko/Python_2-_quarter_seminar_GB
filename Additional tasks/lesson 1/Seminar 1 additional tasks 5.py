"""
Семинар занятие №1
Дополнительные задания:
5)Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""
print("Enter the coordinates of the point A")
coordinates_a = (int(input()), int(input()))
print("Enter the coordinates of the point B")
coordinates_b = (int(input()), int(input()))
print(f"A {coordinates_a}")
print(f"B {coordinates_b}")
# Установлена библиотека NumP
import numpy as np
# Инициализация точек
point_1 = np.array(coordinates_a)
point_2 = np.array(coordinates_b)
# Расчет дистанции функцией np.linalg.norm()
distance = np.linalg.norm(point_1-point_2)
print(f"Distance: {distance}")
