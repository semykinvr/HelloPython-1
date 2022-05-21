# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import os
import random
os.system("cls")

# ВАРИАНТ (короткий код): 
n = random.randint(3, 7)
spisok = [i for i in range(-n,n+1)]
print('список из элементов от -N до N:', spisok)

with open('text17.txt', 'w') as positions:
     for i in range(0, int(n/2)):
         positions.write(f'{random.randint(0, len(spisok))}\n') 

multiply=1
with open('text17.txt', 'r') as positions:
    for element in positions:
        print(f'Позиция: {element}', end='')
        multiply = multiply * spisok[int(element.strip())]
print(f'Произведение элементов на этих позициях = {multiply}\n')



# # ВАРИАНТ (длинный код):
# # функция генерирует рандомное ЦЕЛОЕ ЧИСЛО:
# import random
# def Get_random_int(): return random.randint(1, 9)

# n = Get_random_int()
# print(f'Задан диапазон от {-n} до {n}:')
# spisok=[]
# for i in range(-n, n+1):
#     spisok.append(i)
# print(spisok)

# # ввод позиций с клавиатуры:
# pos=input(f'Введите, через запятую, позиции элементов которые необходимо перемножить, не более {n*2}: ').split(',')
# print(type(pos))
# print('введены вот эти позиции:', pos)
# # запись в файл
# with open('positions.txt', 'w') as positions:
#     for i in pos:
#         positions.write(f'{i}\n') 

# multiply=1

# with open('positions.txt', 'r') as positions:
#     for element in positions:
#         multiply = multiply * spisok[int(element.strip())]

# print(f'Произведение элементов на этих позициях = {multiply}')


# # читаем ('r') числа из текстового файла записываем в массив
# # with open('1.txt', 'r') as F:
# #     v=[]
# #     for x in F:
# #         v.append(int(x))
# # print(v)