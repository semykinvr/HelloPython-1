# 54. Задача: Интерполировать стоимость 1 квадратного метра квартиры, если известно, например, что есть такие квартиры: 
# 31м**2 = 19240$, 
# 51м**2 = 30500$, 
# 61м**2 = 55555$,
# 71м**2 = 60000$,
# 81м**2 = 70000$,
# 91м**2 = 80000$,   
# Нарисовать график.
# Cколько будет стоить квартира 63м**2 ?

# pip3 install sympy
# pip3 install scipy
# pip3 install numpy

import matplotlib.pyplot as plt
from sympy import *
from scipy import interpolate

x_values = [31, 51, 61, 71, 81, 91]
y_values = [19240, 30500, 55555, 60000, 70000, 80000]
#x_values = list(range(1,1001))
#y_value = [15*x**2 for x in x_values]
#y_value = [x**2 for x in x_values]
f = interpolate.interp1d(x_values, y_values, fill_value="extrapolate")

# вероятно это описание окна с графиком
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# назначение заголовка диаграммы и меток осей
ax.set_title("зависимость стоимости квартиры от метража", fontsize = 16)
ax.set_xlabel("метров квадратных", fontsize = 14)
ax.set_ylabel("стоимость в долларах", fontsize = 14)
# размер шрифта для делений на осях
ax.tick_params(axis = 'both', which='major', labelsize = 14)

# назначение диапазона для каждой оси
ax.axis([0, 100, 0, 100000]) # от 0 до 100м**2,  от 0 до 100 000 $

# вызов программы распечатки графика
x1 = range(31, 91)
#plt.plot(x_values, y_values, 'o', x1, f(x1), '--')
plt.plot(x_values, y_values, 'o')
plt.plot(x1, f(x1), '--')
plt.show()

plt.savefig('task54.png', bbox_inches='tight')



