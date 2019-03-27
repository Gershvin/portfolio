"""
Алгоритм программы:
1) создание случайного массива, его интерполяция по методу Лагранжа
2) создание функции на основе интерполяции
3)
"""


import numpy as np
import random

d = 0.1          #шаг численнного интегрирования
s1 = 0           #интеграл первого полинома
s2 = 0           #интеграл второго полинома

def integral(y1, y2): #функция расчёта интегралов
    for i in range(a, b):
        func1 = random.uniform(0, 150)
        func2 = random.uniform(0, 150)
        s1 = s1 + d * y1*y2
        i = i + d
        if y1 == y2:
            return(s1)
        else:
            return(s2)

a = int(input('введите левый предел '))
b = int(input('введите правый предел '))
D = 1/(b-a)
corr = D*integral(func1, func2) / (abs(D)*(pow(integral(func1, func1)*integral(func2, func2)), 0.5))




