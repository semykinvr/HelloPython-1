
from datetime import datetime, date

def log_to_file(surname, name, phone, comment, variant):
    if variant == '1':
        with open('vertical.csv', 'a', encoding='utf-8') as file:
            file.write(f'{date.today()}\n{surname}\n{name}\n{phone}\n{comment}\n\n')
    elif variant == '2':
        with open('horizontal.csv', 'a', encoding='utf-8') as file:
            file.write(f'{date.today()};{surname};{name};{phone};{comment}\n')
    
