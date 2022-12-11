"""
Сложность данной функции O(n^2) поскольку имеет вложенный цикл.
Функция возвращает 
"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: TreeNode) -> List[float]:
    stack = [root]
    res = []
    while stack:                       #
        tem = []                       # Создаем пустой список.
        value = 0                      # Создаем переменная с значением 0.
        for i in stack:                # Создаем цикл проходящий по дереву.
            if i.left:                 # если у элемента дерева есть значение слева,
                tem.append(i.left)     # То к списку прибавляет это самое значение.
            if i.right:                # Тоже самое и справа.
                tem.append(i.right)
            value += i.val             # К переменной значения присваиваем значение текущей итерации.
        res.append(value / len(stack)) # К Списку прибавляем итоговое значение цикла деленное на длину дерева.
        stack = tem[:]                 # Стеку присваиваем пустой список.
    return res                         # Функция возвращает результат.