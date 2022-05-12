# 30.	Вычислить число π c заданной точностью d Пример: при d = 0.001,π = 3.141.    10^(-1)≤d≤10^(-10)

import os
os.system("cls")
import math

# функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
import random
def Get_random_int(): return random.randint(1,10)

d = Get_random_int()
print(f"Задана точность: {d} - знаков после запятой") 

from math import *
print(f"Округляем число Пи {pi} до {d} знаков после запятой: {round(math.pi,d)}")
