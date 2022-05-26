# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

import os
os.system('cls')

print("Введите x  ")
x = int(input())
print("Введите y  ")
y = int(input())
if (x > 0 and y > 0):
    print("первая четверть")

elif (x < 0 and y > 0):
    print("вторая четверть")

elif (x > 0 and y < 0):
    print("четвертая четверть")

elif (x < 0 and y < 0):
    print("третья четверть")

else:
    print("не является четвертью")