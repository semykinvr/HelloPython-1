my_list = [] # список
my_tuple = () # кортеж
my_dict = {} # словарь
my_set = set() # множество

my_dict['old_key'] = 123
print(my_dict)
my_dict['new_key'] = 321
print(my_dict)
del my_dict['old_key']
print(my_dict)


# РАБОТА С ФАЙЛАМИ
my_text = open('test.txt', 'w')
my_text.write('Привет МИР!')
my_text.close()

my_text = open('test.txt', 'r')
print(my_text.read())
my_text.close()

# чёто не работает это ...
my_text = open('test.txt', 'r+')
print(my_text.write('123\n'))
my_text.close()

my_text = open('test.txt', 'w+')
print(my_text.write('456'))
my_text.close()

my_text = open('test.txt', 'a+')
print(my_text.write('789'))
my_text.close()

