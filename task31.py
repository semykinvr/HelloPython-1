# 31.	Задайте натуральное число N. Составить список простых множителей натурального числа N

import os
os.system("cls")

# функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
import random
def Get_random_int(): return random.randint(2,17)
n = Get_random_int()
print(f"Задано число: {n}") 

spisok=[]
for i in range(2,n):
    while n%i == 0:
        #spisok.insert(0,i)
        spisok.append(i)
        #print(spisok)
        n=n/i
        #print(n)
        
if len(spisok) == 0:
    print(f"Число является простым")
else:
    print(f"Cписок множителей числа: {spisok}")