# 1. По двум заданным числам проверить является ли одно квадратом второго. 

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

# if a == b**2 or b == a**2:
#     print('одно число является квадратом другого\n')
# else:
#     print('числа не являются квадратами друг друга\n')

if a == b ** 2:
    print(f" число {a} является квадратом числа {b}")
elif b == a ** 2:
    print(f" число {b} является квадратом числа {a}")
else :
    print("числа не являются квадратами друг друга")