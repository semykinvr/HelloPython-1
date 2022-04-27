# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности (3n + 1). например Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# функция ввода ЦЕЛОГО ЧИСЛА с клавиатуры:
def Input_int():
    while True:
        try:
            console_input = int(input("Введите целое число: "))
            return int(console_input)
        except ValueError:
            print("Неверный ввод.")

n = abs(Input_int())
slovar1 = {} # определяем словарь1
slovar2 = {} # определяем словарь2
for i in range(1,n+1):
    slovar1[i] = 3*i+1          # i-ключ, (3*i+1)-значение к этому ключу
    slovar2.update({i:3*i+1})   # i-ключ, (3*i+1)-значение к этому ключу

slovar3 = {j: (3 * j + 1) for j in range(1, n+1)} # j-ключ, (3*j+1)-значение к этому ключу

print (type(slovar1))
print ('Словарь1', slovar1)
print (type(slovar2))
print ('Словарь2', slovar2)
print (type(slovar3))
print ('Словарь3', slovar3)
