# 4. Показать первую цифру дробной части числа 

# способ МАТЕМАТИЧЕСКИЙ 1
from random import uniform
n = uniform(0, 10)
print('Дано число: ', n)
nn = int((n*10)%10)
print('первая цифра дробной части: ',nn,'\n')

# способ МАТЕМАТИЧЕСКИЙ 2
n = abs(float(input('Введите число с дробной частью: ')))
nn = int((n*10)%10)
print('Первая цифра дробной части: ',nn,'\n')



# способ СТРОКОВЫЙ
n = float(input('введите дробное число: '))

n1 = str(float(n))
print('type n1', end=' - ') 
print(type(n1))
print('распечатываем n1= ', n1)

n2 = n1.split('.')
print('type n2', end=' - ') 
print(type(n2))
print('распечатываем n2= ', n2)

n3 = n2[1]
print('type n3', end=' - ') 
print(type(n3))
print('распечатываем n3= ', n3)

n4 = n3[0]
print('type n4', end=' - ') 
print(type(n4))
print('первая цифра дробной части числа: ', n4)





# n=20.454573
# print(int(n*10)%10)
