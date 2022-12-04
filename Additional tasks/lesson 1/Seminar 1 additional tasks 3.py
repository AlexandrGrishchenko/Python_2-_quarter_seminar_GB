"""
Семинар занятие №1
Дополнительные задания:
3)Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3.
"""
coordinates_x = int(input("Введите координаты оси Х:\t"))
coordinates_y = int(input("Введите координаты оси Y:\t"))
if coordinates_x == 0 or coordinates_y == 0:
    print("Точка имеет нулевую коодринату")
    if coordinates_x ==0:
        print("Точка находится на оси Х")
    else:
        print("Точка находится на оси Y")
elif coordinates_x > 0 and coordinates_y > 0:
    print(f"Точка {coordinates_x, coordinates_y} имеет 1 четверть плоскости")
elif coordinates_x < 0 and coordinates_y > 0:
    print(f"Точка {coordinates_x, coordinates_y} имеет 2 четверть плоскости")
elif coordinates_x < 0 and coordinates_y < 0:
    print(f"Точка {coordinates_x, coordinates_y} имеет 3 четверть плоскости")
elif coordinates_x > 0 and coordinates_y < 0:
    print(f"Точка {coordinates_x, coordinates_y} имеет 4 четверть плоскости")
