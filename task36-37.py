# 36. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
# 37. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7] Порядок элементов менять нельзя
from random import *
import os
os.system("cls")
print('\n\n')

nums = [randint(1, 9) for i in range(10)]
print('\nЗадан список: ', nums)

# функция возвращает возрастающую последовательность из заданного на вход списка чисел: 
def get_up_spisok(nums):
    up_spisok = [nums[0]]
    m = max(up_spisok) 
    for i in nums:
        if i > m:
            up_spisok.append(i)
            m = max(up_spisok) 
    return up_spisok

print('\nВозрастающие последовательности из этого списка: ')
largest = 0
index = 0
massiv_spiskov = [] 
max_dlinna_spiska = 1
for i in range(len(nums)):
    i_spisok = get_up_spisok(nums[i:])
    if len(i_spisok) > max_dlinna_spiska : 
        max_dlinna_spiska = len(i_spisok) # запоминаем максимальную длинну скиска
    print(i_spisok)
    massiv_spiskov.append(i_spisok) # создаём массив из набора возрастающих списков

print('\nМассив из этих списков: ')
for i in range(len(massiv_spiskov)):
    print(massiv_spiskov[i])

print('\nВозрастающий Список или Списки с максимальным количеством элементов: ')
for i in range(len(massiv_spiskov)):
    if max_dlinna_spiska == len(massiv_spiskov[i]): 
        print(massiv_spiskov[i])
