def f(x):
    return x**2

ff = f

print(type(f))
print(type(ff))

print('\n')

print(f(2))
print(ff(2))

############################################################
# ФУНКЦИЮ def МОЖНО ЗАМЕНИТЬ НА LAMBDA
def f(x,y):
    return x + y

F = lambda x,y: x+y # получилось тоже самое что и def
#############################################################


#########################################################
# встроенная функция zip
users = ['name1','name2','name3'] 
id = [11,22,33]
spisok = list(zip(users,id))
print(spisok) # возвращает кортеджи (name,id)

#########################################################
# встроенная функция enumerate
users = ['name1','name2','name3'] 
spisok = list(enumerate(users))
print(spisok) # возвращает кортеджи (ИНДЕКС, name)

#########################################################
# встроенная функция filter
# например функция f(x) - ищет чётные числа
# тогда 
# filter(f, [1, 2, 3, 4, 5])
# возвращает список с чётными числами
#           [   2,    4   ]

############################################################
# как проверить при вводе int(input()) что ввели цифру а не букву: 
# https://metanit.com/python/tutorial/2.11.php
# 1 вариант:
# n = input('Введите число N: ')
# while n.isdigit() != True:
#     n = input('Вы ввели что-то не то. Повторите ввод: ')
# if n.isdigit() == True:
#     n=int(n)

# 2 вариант
# def isdigit(value):
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False

# while True:
#     a = input('Введите число: \n')
#     if isdigit(a):
#         b = int(a)
#         break
#     else:
#         print('Некорректный ввод. Повторите')
############################################################
