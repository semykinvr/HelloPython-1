# 11. Сформировать список из N членов последовательности. Например для N = 5:  1, -3, 9, -27, 81 и т.д.

# 1 ВАРИАНТ (короткий код): 
spisok = [(-3) ** i for i in range (int(input('Введите количество элементов: ')))]
print(spisok)




# # 2 ВАРИАНТ (длинный код): 
# # функция ввода ЦЕЛОГО ЧИСЛА с клавиатуры:
# def Input_int():
#     while True:
#         try:
#             console_input = int(input("Введите целое число: "))
#             return int(console_input)
#         except ValueError:
#             print("Неверный ввод.")

# print('Введите кол-во элементов ')
# n = abs(Input_int())
# massiv = []
# for i in range(0, n):
#     massiv.append((-3)**i)   # Добавление элемента в конец списка
# print(f"Сформированный список: {massiv}") 

