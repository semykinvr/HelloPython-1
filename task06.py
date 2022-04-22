# 6.	Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

# функция ввода ЦЕЛОГО ЧИСЛА с клавиатуры:
def Input_int():
    while True:
        try:
            console_input = int(input("Введите число: "))
            return int(console_input)
        except ValueError:
            print("Неверный ввод.")


week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

print('Введите число, обозначающее день недели: ')

while True:
     day = Input_int()
     if 1 <= day <= 7: break

if 1 <= day <= 5:
     print(f'Это {week[day - 1]} - будний день')
if 6 <= day <= 7:
     print(f'Это {week[day - 1]} - выходной день')
