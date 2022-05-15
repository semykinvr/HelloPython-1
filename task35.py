# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти это число. 
from random import *
import random
import os
#import io
os.system("cls")

# очищаем файл
data = open('text35.txt', 'w')
data.close()

# ЗАПИСЫВЕМ В ФАЙЛ последовательность
d = random.randint(2,50) # первый элемент последовательности задан рандомно
data = open('text35.txt', 'a') 
data.write(str(d))
r = random.randint(2,10) # рандомно задаём позицию элемента, который нужно исключить из списка
for i in range (1, 11):
    if i != r : data.write(' ' + str(d+i)) # один элемент исключаем из списка
data.close

# СЧИТЫВАЕМ ИЗ ФАЙЛА В ПЕРЕМЕННУЮ И ПЕЧАТАЕМ ЕЁ:
with open('text35.txt', 'r') as data:
    stroka = data.read() 
    print(type(stroka))
    print('В файле записана следующая строка', stroka)

# перевели строку в массив 
spisok = stroka.split(' ')
print(type(spisok))
print("список для перебора: ", spisok)

for i in range(1, len(spisok)):
    if (int(spisok[i]) - 1) != (int(spisok[i - 1])):
        print('В последовательности не хватает числа:', int(spisok[i]) - 1)
