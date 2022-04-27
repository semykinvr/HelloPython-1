# 16. Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму

# функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
import random
def Get_random_int(): return random.randint(1, 9)

n = Get_random_int()
print(f'Задано число: {n}')

massiv = []

for i in range(1, n+1):
    massiv.append(1+(1/i)**i)
print(massiv)
print(f'Сумма чисел в последовательности: {round(sum(massiv), 2)}')
