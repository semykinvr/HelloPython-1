# 53. Задача: 
# Дана функция f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 1.	Определить корни
# 2.	Найти интервалы, на которых функция возрастает
# 3.	Найти интервалы, на которых функция убывает
# 4.	Построить график
# 5.	Определить промежутки, на котором f > 0
# 6.	Определить промежутки, на котором f < 0
# Полезная ссылка для работы с matplotlib
# https://devpractice.ru/matplotlib-lessons

# Для математических функций
# !!! Установка jupyter и sympy:
# pip3 install jupyter
# pip3 install sympy
# pip3 install matplotlib

from sympy import *
from jupyter import *
from matplotlib import *

# https://habr.com/ru/post/423731/
def f():
    x = Symbol('x')
    return -18*x**3 + 5*x**2 + 10*x - 30 # возвращает эту строку
    #return -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30 # очень много вычислений, зависает

def ff(xx):
    return float(-18*xx**3 + 5*xx**2 + 10*xx - 30) # возвращает значение функции в точке xx
    #return float(-12*xx**4*sin(cos(xx)) - 18*xx**3+5*xx**2 + 10*xx - 30) # очень много вычислений, зависает

# solve - переводится как "РЕШАЙ!"
y = solve(f()) #возвращает список с конями уравнения (корни комплексные нужно перевести их во флоат).
print('корни: \n', y)

df=diff(f()) # получаем дифференциал этого уравнения 
print('дифференциал уравнения: ', df)
korni = solve(df) #получаем корни этого уравнения
print('корни ДИФФ: ', korni)

# 2.	Найти интервалы, на которых функция возрастает
print('интервалы, на которых функция возрастает: ', solve(df>0)) #
# 3.	Найти интервалы, на которых функция убывает
print('интервалы, на которых функция убывает: ', solve(df<0)) #
# 5.	Определить промежутки, на котором f > 0
print('промежутки, на котором f > 0 :', solve(f()>0))
# 6.	Определить промежутки, на котором f < 0
print('промежутки, на котором f < 0 :', solve(f()<0))

# 4.	Построить график
# для построения графика:
import matplotlib.pyplot 
list_y=[]
for i in range(-10, 11): # берём короткий отрезок по оси х, от -10 до 10
    x5=i
    y5= ff(x5)
    list_y.append(y5)
print('дискретные точки х и y для отрисовки графика: \n', list_y, "\n") # получили дискретные точки х и y для отрисовки графика

matplotlib.pyplot.plot(range(-10,11), list_y) # передали эти точки в функцию, которая строит по ним график
