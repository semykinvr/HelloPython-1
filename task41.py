# 41. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# 	  входные и выходные данные хранятся в отдельных текстовых файлах
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные: 
# 12W1B12W3B24W1B14W

# СЖАТИЕ:
with open('text41_in.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
with open('text41_in.txt', 'r') as data:
    stroka = data.readline()

print('\nИсходная (не сжатая) строка в файле: ', stroka)

count = 1
new_stroka = ""
for i in range(len(stroka)-1):
    if stroka[i] == stroka[i + 1]:
        count = count + 1
    else:
        new_stroka = new_stroka + str(count) + stroka[i]
        count = 1
new_stroka = new_stroka + str(count) + stroka[i]

with open('text41_out.txt', 'w') as data:
    data.write(new_stroka)
with open('text41_out.txt', 'r') as data:
    new_stroka2 = data.readline()

print('Сжатая строка в файле:               ', new_stroka2)


# РАЗЖАТИЕ (РАСШИФРОВКА)
count = ''
result = ''
for i in new_stroka2:
    if i.isdigit():
        count = count + i
    else:
        result = result + i * int(count)
        count = ''

with open('text41_out.txt', 'w') as data:
    data.write(result)
with open('text41_out.txt', 'r') as data:
    new_stroka3 = data.readline()

print('Разжатая строка в файле:             ', new_stroka3, '\n')
