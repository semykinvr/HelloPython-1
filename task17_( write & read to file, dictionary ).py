# ЧТЕНИЕ И ЗАПИСЬ В ФАЙЛ ИЗ СЛОВАРЯ

# СЛОВАРЬ:
slovar = {
     1: 'ONE',
     2: 'TWO',
     3: 'THRE'
}
for i in slovar: 
    print(i, ' - ', slovar[i])

# ЗАПИСЫВАЕМ ЗНАЧЕНИЯ ИЗ СЛОВАРЯ В ФАЙЛ, НА КАЖДУЮ СТРОЧКУ ОТДЕЛЬНО:
data = open ('text17_().txt', 'w')
for i in slovar: 
    data.write(f'{slovar[i]}\n')
    #data.write(' ')
data.close()

path = 'text17_().txt'

# ДОПИСЫВАЕМ ЗНАЧЕНИЕ В ФАЙЛ, НА НОВУЮ СТРОЧКУО:
with open(path, 'a') as data:
    data.write('FOOR\n') 
    
# вариант1:
# with open(path, 'r') as data:
#     for i in data: # СЧИТЫВАЕМ КАЖДУЮ СТРОКУ ОТДЕЛЬНО
#         print(i, end='') # ПЕЧАТАЕМ КАЖДУЮ СТРОКУ ОТДЕЛЬНО

# вариант2:
# СЧИТЫВАЕМ ИЗ ФАЙЛА В ПЕРЕМЕННУЮ И ПЕЧАТАЕМ ЕЁ:
with open(path, 'r') as data:
    all_data = data.read() 
    print(type(all_data))
    print(all_data)

# для записи всего словаря в файл (сразу), использовать нужно pickle