import os
import random
os.system("cls")

def initial():
    #a = input('Введите первое число: ')
    #a = random.randint(-9, 9)
    a = round(random.uniform(-9, 9), 2)
    print('Задано А = ', a)
    #b = input('Введите второе число: ')
    #b = random.randint(-9, 9)
    b = round(random.uniform(-9, 9), 2)
    print('Задано B = ', b)
    
    #operation = input("Введите операцию ( + , - , / , *): ")
    operation_list = ( '+' , '-' , '/' , '*')
    operation = operation_list[random.randint(0, 3)]
    print('Задана операция: ', operation)

    #return [a, b, operation] # возвращаем кортеж(или список)
    return (a, b, operation) # возвращаем кортеж(или список)