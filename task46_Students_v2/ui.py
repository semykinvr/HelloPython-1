from get_push_data import get_data
from add_data import add_data


def operations():
    print('Введите: \n1 - получаем информацию об учениках (get_data()) \n2 - добавляем ученика add_data() \n3 - выходим из программы\n')
    a = input('Выберите действие: ')
    # while (a != '1' or a != '2'):
    #     a = input('Введите (1) или (2):')
    if a == '1':
        #print(*get_data())
        print(*get_data())
        #operations()
    if a == '2':
        add_data()
        #operations()
    if (a != '1') and (a != '2'):
        exit()
