def f(x):
    return x**2

ff = f

print(type(f))
print(type(ff))

print('\n')

print(f(2))
print(ff(2))

############################################################
# ФУНКЦИЮ def МОЖНО ЗАМЕНИТЬ НА LAMBDA
def f(x,y):
    return x + y

F = lambda x,y: x+y # получилось тоже самое что и def
#############################################################


#########################################################
# встроенная функция zip
users = ['name1','name2','name3'] 
id = [11,22,33]
spisok = list(zip(users,id))
print(spisok) # возвращает кортеджи (name,id)

#########################################################
# встроенная функция enumerate
users = ['name1','name2','name3'] 
spisok = list(enumerate(users))
print(spisok) # возвращает кортеджи (ИНДЕКС, name)
