# 12.1 
# Сделать СЛОВАРЬ: id, name, date 
# выполнить действия с данными: посмотреть (по id), добавить, удалить. 

# !это словарь из словарей:
slovar = {
    1: {'name': 'киви', 'date': 20220428 }
}

while True:
    print('введите номер операции 1-просмотр, 2-добавление, 3-удаление, 4-выход')
    n = int(input())
    if n==1:
        id = int(input('введите id: '))
        print(slovar[id])
    elif n == 2:
        id = int(input('введите id: '))
        name = input('введите name: ')
        date = int(input('введите date: '))
        slovar[id] = {'name': name, 'date': date } # добавление в словарь "подСловаря"
    elif n==3: 
        id = int(input('введите id: '))
        del slovar[id] # удаление из словаря
    elif n==4: break

print(slovar)

