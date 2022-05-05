# 23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#Пример: 
# [2, 3, 4, 5, 6] => [12, 15, 16]; 
# [2, 3, 5, 6] => [12, 15] 

# функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
import random
def Get_random_int(): return random.randint(5,11)
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

spisok2 = []
for i in range ( 0, ((len(spisok) + 1)//2) ):
    spisok2.append(spisok[i] * spisok[-1-i]) 
print(f"Результат: \n{spisok2}")
