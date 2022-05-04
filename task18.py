# 18. Реализовать алгоритм перемешивания списка. 


# функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
import random
def Get_random_int(): return random.randint(1, 99)

n = Get_random_int()
print(f'Задан список от 0 до {n}:')
massiv = list(range(0, n + 1))
print(massiv)

from random import shuffle
shuffle(massiv)
print('Список перемешан:')
print(massiv)