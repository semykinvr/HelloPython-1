# 22. Задайте список из нескольких чисел. Найти сумму чисел списка стоящих на нечетной позиции. 

# функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
import random
def Get_random_int(): return random.randint(10, 21)
# задаём длинну списка:
n = Get_random_int()
print(f"Задана длинна списка: {n}")

from random import *
# заполняем массив:
spisok = []
# for i in range(0, n):
#     spisok.append(random.randint(1,10))
spisok = [randint(1, 9) for i in range(0,n)]
print(f"Создан рандомный список: \n{spisok}")

# sum = 0
# for i in range(1, len(spisok), 2):
#     sum = sum + spisok[i]
# print(f"Сумма чисел списка стоящих в нечетных позициях = {sum}")
print('Сумма элементов на нечетных позициях равна ', sum(spisok[1::2]), '\n')

