# 33. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

# k = (int(input("Введите натуральную степень k = ")))
k = 3

# ЗАПИСЫВЕМ В ФАЙЛ
data = open('text33.txt', 'a') # a - добавить, w - перезаписать, r - чтение
for i in range (k,0,-1):
    # случ коэффициент умножить на x в степени k плюс
    c = random.randint(0,100)
    data.write(f'{c}x^{i} + ')
data.write(f'{random.randint(0,100)} = 0\n')
data.close

# СЧИТЫВАЕМ ИЗ ФАЙЛА В ПЕРЕМЕННУЮ И ПЕЧАТАЕМ ЕЁ:
with open('text33.txt', 'r') as data:
    stroki = data.read() 
    print(type(stroki))
    print(stroki)