"""
Семинар занятие №2
Базовые задания
4) Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
print("Введите строку из нескольких слов")
text = input()
new_text = text.split(' ')
for ind, el in enumerate(new_text, 1):
    print(ind, el[:10])

