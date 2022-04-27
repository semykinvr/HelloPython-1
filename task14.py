# 14. Подсчитать сумму цифр в вещественном числе

# функция генерирует рандомное ВЕЩЕСТВЕННОЕ ЧИСЛО:
import random
def Get_random_float(): return random.uniform(1, 999)


# 1 вариант:
a = float(Get_random_float()) # задаем случайное вещественное число из диапазона
f = a
print('Задано число:', a,'\n')


a = str(a).replace('.', '') # переводим в строковый тип, убираем точку
d = a
e = int(a)
print(type(a))
print('убрали точку и сделали строку', a,'\n')

b = map(int, a) # перевели строку в объект
print(type(b))
print('перевели строку в объект ', b,'\n')

с = list(b) # переводим объект в массив
print(type(с))
print('переводим объект в массив', с,'\n')

summa = sum(с) # считаем сумму
print('1: Сумма цифр данного числа равна: ', summa, '\n')


# 2 вариант:
massiv = []
for i in range(0, len(d)): massiv.append(int(d[i])) # Добавление элемента в конец списка
print(massiv)
print('2: Сумма цифр данного числа равна: ', sum(massiv), '\n')

# 3 вариант:
summa = 0
while e > 0:
    summa = summa + (e % 10)
    e = e // 10
print(f'3: Сумма цифр данного числа равна: {summa} \n')

# 4 вариант:
massiv4 = list(str(f).split('.'))
summa = 0
for i in massiv4:
    for j in i:
        summa = summa + int(j)
print(f'4: Сумма цифр данного числа равна: {summa} \n')

# 5 вариант:
summa = 0
for i in d:
    summa = summa + int(i)
print(f'5: Сумма цифр данного числа равна: {summa} \n')