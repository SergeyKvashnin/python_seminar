# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

import os
os.system('cls')

print("Задайте номер четверти: ")
chetvert = int(input())

if (chetvert == 1 ):    #(x > 0 && y > 0)

    print("первая четверть")
    print("диапазон: х от 0 до ∞ ")
    print("диапазон: y от 0 до ∞")

elif (chetvert == 2):     #(x < 0 && y > 0)
    print("вторая четверть")
    print("диапазон: х от 0 до - ∞")
    print("диапазон: y от 0 до ∞")

elif (chetvert == 3):    #(x > 0 && y < 0)
    print("четвертая четверть")
    print("диапазон: х от 0 до ∞")
    print("диапазон: y от 0 до - ∞")

elif (chetvert == 4):   #(x < 0 && y < 0)
    print("Третья четверть.")
    print("диапазон: х от 0 до - ∞")
    print("диапазон: y от 0 до - ∞")

else: 
    print("четверть введена не верна")