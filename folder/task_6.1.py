# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
import os
os.system("cls")

week = ['понедельник', 'вторник', 'среда',
        'четверг', 'пятница', 'суббота', 'воскресенье']
n = input('Введите число, обозначающее день недели: ')
while n != '1' and n != '2' and n != '3' and n != '4' and n != '5' and n != '6' and n != '7' :
    n = input(
        'Ошибка, число должно быть в диапазоне от 1 до 7. \nВведите число, обозначающее день недели: ')
else:
    n = int(n)
    print(f'Это', week[n-1], end=', ')
if 1 <= n <= 5:
    print('рабочий день!\n')
else:
    print('выходной день!\n')