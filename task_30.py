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