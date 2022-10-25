"""
Функция имеет сложность O(n) Поскольку имеет лишь 1 цикл завсящий от значения num.
Код проверяет на четность кол-во команд, если четное, то кол-во команд делят на 2, половина проходит, 
а вторая прибавляется к кол-ву совпадений(matches).
Если число команд нечетное, то это число делится на 2 + 1 и итог прибавляется к совпадениям(matches)
"""

def numberOfMatches(num):
    matches = 0
    while num > 1:                  # Цикл работает пока кол-во команды не станет единицей
        if num % 2 == 0:            # Если четное кол-во команд
            matches += num // 2     # к сумме объединенных команд прибавляется n / 2
            num = num // 2          # n / 2 команд проходят в следующий раунд
        else:
            matches += num // 2 + 1 # Если нечетное, то к кол-ву объединений прибавляется частное кол-ва команд на 2 + 1
            num = num // 2          # Затем подсчитваем кол-во команд, проходящих дальше
    return matches

print(numberOfMatches(14))


"""
Исходя из примеров вывода в условии задачи, то можно заметить, что если отнять единицу из задаваемого кол-ва команд(совершенное любое число), 
то мы получим искомый результат - кол-во объединений команд
Тогда сложность функции будет O(1) поскольку из любого числа вычитается константа 1.
"""

def matches(x):
    return x-1
print(matches(14))