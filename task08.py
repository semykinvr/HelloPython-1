# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

# функция генерирует рандомное ВЕЩЕСТВЕННОЕ ЧИСЛО:
import random
def Get_random_float(): return random.uniform(-10, 10)


x = round(float(Get_random_float()), 2)
y = round(float(Get_random_float()), 2)
#x = 0.0
#y = 0.0
print(f'Задана координата X: {x}')
print(f'Задана координата Y: {y}')

if(x == 0 and y == 0):
    print("Точка лежит в начале координат")
elif(x == 0):
    print("Точка лежит на оси X")
elif(y == 0):
    print("Точка лежит на оси Y")
elif(x > 0 and y > 0):
    print("Номер четверти: 1")
elif (x < 0 and y > 0):
    print("Номер четверти: 2")
elif (x < 0 and y < 0):
    print("Номер четверти: 3")
else:
    print("Номер четверти: 4")