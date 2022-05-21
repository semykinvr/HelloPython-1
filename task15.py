# 15. Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]


# ВАРИАНТ (короткий код): 
import os
import random
os.system("cls")

n = random.randint(6, 10)
print(f'Задано число N: {n}')
massiv = [1]
for i in range(2, n+1):
    massiv.append(massiv[i-2]*i)
print(massiv, '\n')




# # # ВАРИАНТы (длинный код):
# # функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
# import random
# def Get_random_int(): return random.randint(1, 9)

# n = Get_random_int()
# print(f'Задано число: {n}')
# massiv = [1]

# for i in range(2, n+1):
#     massiv.append(i * massiv[i-2])

# print(massiv)