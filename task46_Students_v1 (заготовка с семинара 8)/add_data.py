def add_data():
    with open('name.csv','r') as name:
        data=name.read()
    Id=len(data)
    list[0]=Id     # list[0] - это Id ученика
    list[1]=input('Введите Фамилию')
    list[2]=input('Введите Имя')
    list[3]=input('Введите Класс')
    list[4]=input('Введите Статус')
    list[5]=input('Введите Ряд')
    list[6]=input('Введите Номер парты')
    list[7]=input('Введите Город')
    list[8]=input('Введите Улица')
    list[9]=input('Введите Дом')
    list[10]=input('Введите Квартира')
    list[11]=input('Введите Примечание')