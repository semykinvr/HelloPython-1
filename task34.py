# 34. Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

import os
os.system("cls")

# Берём данные из 1 файла
# a - добавить, w - перезаписать, r - чтение
data = open('text34-1.txt', 'r') 
stroka1 = str(data.readline())
stroka1 = stroka1.replace("=0","") # Убираем лишнее
stroka1 = stroka1.replace("= 0","") # Убираем лишнее
print(stroka1)
data.close

# Берём данные из 2 файла
data = open('text34-2.txt', 'r')
stroka2 = str(data.readline())
print(stroka2)
data.close

# объединяем две строки и записываем результат в файл
s1_s2 = stroka1 + '+ ' + stroka2
print (s1_s2)

data = open('text34-3.txt', 'w') 
data.write(s1_s2)
data.close

# СЧИТЫВАЕМ ИЗ ФАЙЛА В ПЕРЕМЕННУЮ И ПЕЧАТАЕМ ЕЁ:
with open('text34-3.txt', 'r') as data:
    stroki = data.read() 
    print(type(stroki))
    print(stroki)