# 24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
import random
def Get_random_int(): return random.randint(5,9)
# задаём длинну списка:
n = Get_random_int()
print(f"Задана длинна списка: {n}")

from random import *
# заполняем рандомно массив вещественными числами
spisok = []
# for i in range(0, n):
#     spisok.append(random.randint(1,10))
spisok = [uniform(-11, 11) for i in range(0,n)]
print(f"Создан рандомный список: \n {spisok}")

# убираем целые числа слева от запятой
spisok2 = []
for i in spisok:
    if (abs(i) % 1) != 0: spisok2.append(abs(i) % 1)

print(f"Cписок дробных частей: \n{spisok2}")
print('Максимальное число: ', max(spisok2))
print('Минимальное число:  ', min(spisok2))
print('Разница:            ', max(spisok2) - min(spisok2))

# print('Максимальное число: ', round(max(spisok2), 2))
# print('Минимальное число: ', round(min(spisok2), 2))
# print('Разница: ', round(max(list1) - min(spisok2), 2))
