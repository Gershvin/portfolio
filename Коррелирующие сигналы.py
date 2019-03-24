import numpy as np
import random
import matplotlib.pyplot as plt

def integral(y1, y2): #функция расчёта интегшралов
    for i in range(a, b):
        s1 = s1 + d * y1*y2
        i = i + d

a = np.array([random.random() for i in range(10)])
print(a)
plt.plot([1, 2, 3])

a = input(int('введите начало участка анализа'))
b = input(int('введите конец участка анализа'))
d = 0.1
s1 = 0
s2 = 0
D = 1/(b-a)
y #значение функции в точке
for i in range (a, b):
    s1 = s1+ d*y
    i = i+d

for i in range(a, b):
    s1 = s1 + d*y
    i = i+d
corr = D*integral(func1, func2) / (abs(D)*(pow(integral(func1, func1)*integral(func2, func2)), 0.5))




