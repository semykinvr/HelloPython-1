# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т.е. для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
import random
def Get_random_int(): return random.randint(1,11)
n = Get_random_int()
print(f"Задано число: {n}") 

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, -a)
        a, b = b, a + b
    return fibo_nums

fibo_nums_result = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums_result)
print(type(fibo_nums_result))
print(len(fibo_nums_result))
for j in fibo_nums_result:
    print(fibo_nums_result.index(j), end = ' ')
