# 14. Подсчитать сумму цифр в вещественном числе

# ВАРИАНТ (короткий код): 
spisok = list(map(int, str(input('Введите число: ')).replace('.', ''))) 
print('Сумма цифр данного числа равна:', sum(spisok), '\n')



# # # ВАРИАНТы (длинный код):
# # функция генерирует рандомное ВЕЩЕСТВЕННОЕ ЧИСЛО:
# import random
# def Get_random_float(): return random.uniform(1, 999)

# # 1 вариант:
# n = input('Введите число: ')
# stroka = str(n).replace('.', '') # переводим в строку, убираем точку
# print(stroka)
# stroka2 = list(map(int, stroka)) # переводим в числовой тип, и делаем список
# print(stroka2)
# summa = sum(stroka2) # считаем сумму
# print('Сумма цифр данного числа равна:', summa, '\n')


# # 2 вариант:
# a = float(Get_random_float()) # задаем случайное вещественное число из диапазона
# f = a
# print('Задано число:', a,'\n')

# a = str(a).replace('.', '') # переводим в строковый тип, убираем точку
# d = a
# e = int(a)
# print(type(a))
# print('убрали точку и сделали строку', a,'\n')

# b = map(int, a) # перевели строку в объект
# print(type(b))
# print('перевели строку в объект ', b,'\n')

# с = list(b) # переводим объект в массив
# print(type(с))
# print('переводим объект в массив', с,'\n')

# summa = sum(с) # считаем сумму
# print('1: Сумма цифр данного числа равна: ', summa, '\n')


# # 3 вариант:
# massiv3 = []
# for i in range(0, len(d)): massiv3.append(int(d[i])) # Добавление элемента в конец списка
# print(massiv3)
# print('3: Сумма цифр данного числа равна: ', sum(massiv3), '\n')

# # 4 вариант:
# summa = 0
# while e > 0:
#     summa = summa + (e % 10)
#     e = e // 10
# print(f'4: Сумма цифр данного числа равна: {summa} \n')

# # 5 вариант:
# massiv5 = list(str(f).split('.'))
# summa = 0
# for i in massiv5:
#     for j in i:
#         summa = summa + int(j)
# print(f'5: Сумма цифр данного числа равна: {summa} \n')

# # 6 вариант:
# summa = 0
# for i in d:
#     summa = summa + int(i)
# print(f'6: Сумма цифр данного числа равна: {summa} \n')