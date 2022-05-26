#Вычислить число c заданной точностью d
#Пример:
#при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)
from math import *
print ( pi )
d = float(input('Введите число в диапазоне от 0.1 до 0.0000000001: '))
def counter(d):
    s = str(d)
    if '.' in s:
        return abs(s.find('.') -len(s)) -1
    else:
        return 0
count = counter(d)
print(round(pi, count))

# второе решение

import math
P = 0.001
#P = float(input("Введите количество знаков после запятой для вычисления числа Пи (от 1 до 10 ):\n"))
P = str(P).split('.')
L = len(P[1])
M = str(math.pi)
print(float(M[:L+2]))