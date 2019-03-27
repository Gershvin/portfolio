"""
Алгоритм программы:
1) создание случайного массива, его интерполяция по методу Лагранжа
2) создание функции на основе интерполяции
3)
"""


import numpy as np
import random

def integral(y1, y2): #функция расчёта интегралов
    for i in range(a, b):
        step = 0.1
        func1 = random.uniform(0, 150)
        func2 = random.uniform(0, 150)
        s1 = s1 + d*y1*y2
        s2 = s2 + d*y1*y1
        i = i + step
        if y1 == y2:
            return(s2)
        else:
            s1

a = int(input('введите левый предел '))
b = int(input('введите правый предел '))
D = 1/(b-a)
corr = D*integral(1, 2) / (abs(D)*(pow(integral(1, 1)*integral(2, 2)), 0.5))
print(corr)




