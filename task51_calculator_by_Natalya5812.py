# https://docs-python.ru/packages/modul-slick-python/
# Установка модуля click в виртуальное окружение.
# # создаем виртуальное окружение, если нет:
# $ python3 -m venv .venv --prompt VirtualEnv
# # активируем виртуальное окружение: 
# $ source .venv/bin/activate
# # ставим модуль click:
# (VirtualEnv):~$ python3 -m pip install -U click

# !!! https://tproger.ru/translations/python-command-line-tools-with-click/
# pip install click.


import tkinter  as Tk
import click

root = Tk.Tk()
root.title('Calculator')
root.geometry ('550x450')
root.resizable (False, False)
root.configure (bg = 'black')


buttons = ['7', '8', '9', '+', '*', '4', '5', '6', '-', '/', '1', '2', '3', 'i', '%','.', '0', '±', '=', 'Del', 'CE']
X = 20
Y = 140
for button in buttons:
        get_lbl = lambda x=button: click(x)
        Tk.Button(text = button, bg = 'light grey', font = ('Roboto',20), command = get_lbl).place (x = X, y = Y, width=100, height = 59)
        X +=102
        if X >= 500:
            X = 20
            Y+=60

wind = '0'
global label_text
label_text = Tk.Label (text = wind, bg = 'black', font = ('Roboto', 30), fg = 'white')
label_text.place (x = 20, y = 50)



def click (key):
    global wind 
    global label_text

    if key == 'CE':
        wind = '0'
    elif key == 'Del':
        wind = wind[0:-1]
    elif key == '=':
        wind = str (eval(wind))
    else:
        if wind == '0':
            wind = ''
        wind +=key
    label_text.configure (text=wind)

root.mainloop()
