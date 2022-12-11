"""
Семинар занятие №5
Базовые задания:
2) Создать текстовый файл (не программно), сохранить в нем несколько строк.
Выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('poem.txt', 'r', encoding='UTF-8') as f_obj:
    lines = f_obj.readlines()
    print(f"Всего {len(lines)} строк")
    for key, value in enumerate(lines):
        words = value.split(' ')
        print(f"В {key + 1} строке {len(words)} слов")
