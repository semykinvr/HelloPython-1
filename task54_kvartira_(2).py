# 54. Задача: Интерполировать стоимость 1 квадратного метра квартиры, если известно, например, что есть такие квартиры: 
# 31м**2 = 19240$, 
# 51м**2 = 30500$, 
# 61м**2 = 55555$]  
# Cколько будет стоить квартира 63м**2 ?

from scipy import interpolate

q=63
xp=[31,51,61]
fp=[19240,30500,55555]
f=interpolate.interp1d(xp,fp, fill_value="extrapolate")
print('квартира 63м**2 стоит: ', f(q), ' $')






# import matplotlib.pyplot as plt
# from scipy import interpolate
# from numpy import *
# x = np.arange(5, 20)
# y = np.exp(x/3.0)
# f = interpolate.interp1d(x, y)x1 = np.arange(6, 12)
# y1 = f(x1) # использовать функцию интерполяции, возвращаемую `interp1d`
# plt.plot(x, y, 'o', x1, y1, '--')
# plt.show()