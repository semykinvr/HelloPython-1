#2. Найти максимальное из пяти чисел.  


#первый способ:
from random import randint
n = 5
massiv1 = []
for i in range(0, n):
    massiv1.append(randint(0,100))
print(f'Сгенерирован массив: {massiv1}')
max1 = int(max(massiv1))
print(f'Максимальным числом является: {max1}\n')


#второй способ:
massiv2 = [12,32,16,8,14]
print(f'Задан массив: {massiv2}')
max2 = massiv2[0]
for i in massiv2:
    if i>max2:
        max2=i
print('наибольшее число: ', max2,'\n') 

#третий способ:
n = 5
massiv3 = []
print('Заполните массив: ')
for i in range(0, n):
    massiv3.append((int(input(f'Введите число №{i+1}: '))))
print(f'Вы ввели числа: {massiv3}')
max3 = int(max(massiv3))
print(f'Максимальным числом является: {max3}')