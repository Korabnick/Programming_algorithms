"""
Функция имеет сложность O(n), т.к. имеет единственный цикл, длительность которого зависит от вводимых значений.
Код Проходится по строке с "камнями", если камень является заданным символом, то прибавляет к счетчику бриллиантов +1.
"""

def count_jewels_in_stones2(J, S): # Принимает две строки, в первую пишется то, какие символы будут являтся бриллиантами.
    s_set = set(J)                 # строку с символами бриллиантов объявляем множеством.
    jewels_count = 0               # счетчик найденных бриллиантов.

    for item in S:                 # проходимся по символам в строке с "камнями".
        if item in s_set:          # Если в итерации находится один из введеных символов в "J", то...
            jewels_count += 1      # к счетчику прибавляется 1 бриллиант.
    return jewels_count

print(count_jewels_in_stones2('aA', 'aAAbbbb'))