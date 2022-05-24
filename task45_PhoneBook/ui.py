
def initial ():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите описание: ')
    variant = input('Выберите удобное для вас заполнение (1 - вертикальное, 2 - горизонтальное): ')
    return (surname, name, phone, comment, variant)