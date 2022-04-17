#2. Найти максимальное из пяти чисел.  

massiv1 = [12,32,16,8,14]
print(massiv1)

#первый способ
print('наибольшее число: ', max(massiv1)) 

#второй способ
massiv2 = [12,32,16,8,14]
max2 = massiv2[0]
for i in massiv2:
    if i>max2:
        max2=i
print('наибольшее число: ', max2,'\n') 

#третий способ:
n = 5
massiv3 = []
for i in range(0, n):
    massiv3.append((int(input(f'Введите число №{i+1}: '))))
print(f'Вы ввели числа: {massiv3}')
max3 = int(max(massiv3))
print(f'Максимальным числом является: {max3}')