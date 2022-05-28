import get_data
import add_data

def find():
    a=input('Вы хотите считать информацию (1) или добавить (2)??')
    while a!= '1' or '2':
        a=input('Введите (1) или (2)!!')
    if a==1:
        list=get_data.get_data()
        return list
    if a==2:
        add_data.add_data()