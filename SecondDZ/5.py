"""
Сложность данной функции O(n) поскольку имеет 2 не вложенных цикла, который зависит от длины задаваемого массива.
Функция проходится по длине массива с ценами, в котором проверяется, равна-ли разность предыдущей цены и цены цикла единице.
Если да, то к переменной cur прибавляем единицу, иначе если не равна единице, то к заданному списку добавляем значение
переменной cur, а саму переменную сбрасываем в исходное состояние (1)
Далее цикл, проходящий по итоговому списку прибавляет к переменной результата результат выполнения половины от 
сложения единицы с значением цикла, умножение на это же самое значение
"""

def getDescentPeriods(prices):
    lst = []
    result = 0
    cur = 1
    for i in range(1, len(prices)):      # Цикл проходит по длине массива
        if prices[i-1] - prices[i] == 1: # Если из предыдущего массива отнимаем следующий и он равен единице, то...
            cur += 1                     # к переменной cur прибавляем еденицу
        else:
            lst.append(cur)              # Иначе к списку добавляем это значение и...
            cur = 1                      # переменной cur присваиваем единицу
    lst.append(cur)                      # К итоговому списку прибавляем остаточное значение переменной cur
    for j in lst:                        # Цикл проходящий по получившемуся списку
        result += ((1 + j) * j) // 2     # К переменной результата прибавляем сумму 1 и значение списка умноженное на то же значение и делим все на 2
    return result

print(getDescentPeriods([3,2,1,4]))