# 7.  Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# Преподаватель:
a = [0, 1]
print('X Y Z F')
for x in a:
    for y in a:
        for z in a:
            f = not(x or y or z) == (not x and not y and not z)
            print (x, y, z, f)
print()

# Ещё вариант:
# функция вычисления логического значения
def logic(x1, y1, z1):
    return (not (x1 or y1 or z1) == (not x1 and not y1 and not z1))

a = (True, False)
i = 0
massiv = [] #задаём пустой массив
print('X      Y      Z      F')
for x in a:
    for y in a:
        for z in a:
            massiv.append(logic(x, y, z)) # добавляем в массив значения
            print (x,' ', y,' ', z,' ', massiv[i])
            i=i+1

if (all(j for j in massiv)) == True:
    print('Выражение тождественно')
else:
    print('Выражение НЕ тождественно')
