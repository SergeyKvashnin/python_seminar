# Найти расстояние между двумя точками пространства

import os
os.system('cls')

print('Введите координату х1: ') 
x1 = int(input()) 
print('Введите координату х2: ') 
x2 = int(input()) 
print('Введите координату y1: ') 
y1 = int(input()) 
print('Введите координату y2: ') 
y2 = int(input()) 

A = pow((x2-x1), 2) 
B = pow((y2-y1), 2) 


C = (A+B)**0.5
 
print('расстояние между 2х точек: ', C)