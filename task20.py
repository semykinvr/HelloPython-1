# 20. Определить, присутствует ли в заданном списке строк, некоторое число 


spisok = ['dfgh', '45gh','8sdrr', 'dfh38', '60', 'wrhnm1']
print (f'Cписок: {spisok}')

# функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
import random
def Get_random_int(): return random.randint(1, 9)
# n = Get_random_int()
n = 45
print(f'ищем число {n} в этом списке.')

count = False
for i in range( 0, len(spisok) ):
    if str(n) in spisok[i]:
        print(f'число {n} есть в строке № {i+1}: {spisok[i]}')
        count = True

if count != True:
    print(f'числа {n} нет в списке')


