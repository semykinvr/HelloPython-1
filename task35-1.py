# Задачи с Лекции 3:
# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа). 
# Пример: 1 2 3 5 8 15 23 38 Получить: [(2, 4), (8, 64), (38, 1444)]

# №1
f = open('text35-1.txt', 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e,e **2))
print(out)


# №2
############################################################
# ФУНКЦИЮ def МОЖНО ЗАМЕНИТЬ НА LAMBDA
def f(x,y):
    return x + y

F = lambda x,y: x+y # получилось тоже самое что и def
#############################################################


# №3
def select(f, col): # в метод передаётся функция f и список col
    return [f(x) for x in col]
def where(f, col): # в метод передаётся функция f и список col
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split() # строковый список получаем 
print(data)

res = select(int, data) # челочисленный список получаем
print(res)
res1 = where(lambda x1: not x1 % 2, res) 
print(res1)
res2 = list(select(lambda x2: (x2, x2**2), res1))
print(res2)

#############################################################
# №4
# !!!!!!!!!!!!!!!! ТОЖЕ САМОЕ, НО ЧЕРЕЗ ВСТРОЕННУЮ ФУНКЦИЮ MAP И FILTER !!!!!!!!!!!!!!!!
print('ТОЖЕ САМОЕ, НО ЧЕРЕЗ ВСТРОЕННУЮ ФУНКЦИЮ MAP И FILTER: ')
data = '1 2 3 5 8 15 23 38'.split() # строковый список получаем 
print(data)
data = list(map(int, data))
print(data)
data = list(filter(lambda e: not e % 2, data))
print(data)
data = list(map(lambda e: (e, e**2), data))
print(data)