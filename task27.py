# 27. Строка содержит набор чисел. Показать большее и меньшее число. Символ-разделитель - пробел. 

# СЧИТЫВАЕМ ИЗ ФАЙЛА В ПЕРЕМЕННУЮ И ПЕЧАТАЕМ ЕЁ:
path='text27.txt'
with open(path, 'r') as data:
    spisok = data.read().split(' ') # split - разбиваем строку в строковый массив
print(type(spisok))
print('получился строковый массив: ', spisok)

for i in range(0, len(spisok)):
    spisok[i] = int(spisok[i])
print(type(spisok))
print('получился челочисленный массив: ', spisok)

print('Наибольшее число =', max(spisok))
print('Наименьшее число =', min(spisok))
