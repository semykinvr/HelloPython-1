# 28. Найти корни квадратного уравнения Ax² + Bx + C = 0
#	-Математикой
#	-Используя дополнительные библиотеки Python

from math import *
from random import *
import os
os.system("cls") # очистка экрана
a = round(uniform(-100, 100), 2)
b = round(uniform(-100, 100), 2)
c = round(uniform(-100, 100), 2)
print('a = ', a)
print('b = ', b)
print('c = ', c)

# функция возвращает дискримингант
def deskriminant(a, b, c):
    return b**2-4*a*c
# функция поиска корней уравнения, возвращает кортеж 
def roots(a, b, c):
    d = deskriminant(a, b, c)
    if d < 0:
        print(f'D < 0. Система не имеет решений!\n')
    elif d > 0:
        print(f'D > 0. Система имеет два корня, х1: {(-b-d**0.5)/(2*a):.2f} и х2: {(-b+d**0.5)/(2*a):.2f}\n')
        x1 = round((-b-d**0.5)/(2*a), 4) 
        x2 = round((-b+d**0.5)/(2*a), 4)
        return x1,x2
    else:
        print(f'D = 0. Система имеет один корень, х: {-b/(2*a):.2f}\n')
        x = round((-b/(2*a)), 4)
        return x

print(roots(a,b,c))

