# 10. Найти расстояние между двумя точками пространства

# функция генерирует рандомное ВЕЩЕСТВЕННОЕ ЧИСЛО:
import random
def Get_random_float(): return random.uniform(-10, 10)


# функция вычисляет длинну диагонали куба по формуле:
import math
def Diagonal_kuba(x, y, z): return round(float(math.sqrt(x**2 + y**2 + z**2)), 2)


x1 = Get_random_float()
y1 = Get_random_float()
z1 = Get_random_float()
print(f"Координата первой точки: X1={x1};  Y1={y1};  Z1={z1}")
x2 = Get_random_float()
y2 = Get_random_float()
z2 = Get_random_float()
print(f"Координата второй точки: X1={x2};  Y1={y2};  Z1={z2}")

X = abs(x2-x1); 
Y = abs(y2-y1); 
Z = abs(z2-z1); 
print('длины сторон куба: ',X,Y,Z)

print("Длинна между двумя точками (диагональ куба): ", Diagonal_kuba(X,Y,Z))
