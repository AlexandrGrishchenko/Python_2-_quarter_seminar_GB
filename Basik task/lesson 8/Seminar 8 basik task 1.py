"""
Семинар занятие №8
Базовые задания:
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

import random


class Matrix():

    def __init__(self, lst):
        self.lst = lst
        self.row_count = len(self.lst)
        self.col_count = len(self.lst[0])

    def __str__(self):
        ret_val = ''
        for i in range(self.row_count):
            for j in range(self.col_count):
                ret_val += str(self.lst[i][j]) + '\t'
            ret_val += '\n'

        return ret_val

    def get_item(self, row, col):
        try:
            ret_val = self.lst[row][col]
        except:
            ret_val = 0

        return ret_val

    def __add__(self, other):

        new_lst = []
        max_rows = max(self.row_count, other.row_count)
        max_cols = max(self.col_count, other.col_count)

        for i in range(max_rows):
            new_lst.append([])
            for j in range(max_cols):
                new_lst[i].append(self.get_item(i, j) + other.get_item(i, j))

        return Matrix(new_lst)


max_row = 20
max_col = 20


# Здесь в зависимости от контекста можно было бы в функцию параметрами передавать количество строк и столбцов
# Я решил это сделать через random непосредственно в теле функции
def create_lst():
    rows = random.randint(1, max_row)
    cols = random.randint(1, max_col)
    tmp_list = []
    for i in range(rows):
        tmp_list.append([])
        for j in range(cols):
            tmp_list[i].append(random.randint(0, 99))

    return tmp_list


m1 = Matrix(create_lst())
print(m1)

m2 = Matrix(create_lst())
print(m2)

m3 = m1 + m2
print(m3)
