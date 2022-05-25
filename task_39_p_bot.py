# 39.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

from random import *

konfet = int(input('Введите количество конфет для игры: \n'))
print()
Name = input('Введите ваше имя: \n')
print()
print(f'Если выпадает цифра 1 - первый ходит {Name}, если цифра 2 - первым ходит bot')
print()
x = randint(1, 2)    # Рандом определяет кто ходит первым
print(f'Прошла жеребьевка, выпала цифра: {x}')
print()
if x == 1:          # Если первым ходит plauer_1
    plauer = int(input(
        f'Первым ходит {Name}. Возьмите количество конфет, не превышающее 28 штук: \n'))
    while plauer <= 0 or plauer > 28:
        plauer = int(input(
            f'{Name} вы ввели не вернау цифру, повторите ввод в диапазоне цифр от 1 до 28 включительно: \n'))
    konfet -= plauer
    #print(f'Вы взяли {plauer} конфет')
    while konfet > 28:
        if (1 < plauer < 12 and 35 <= konfet <= 56) or (19 < plauer < 29 and 35 < konfet <= 56):
            bot = randint(1, 8)
            print(f'bot взял {bot} конфет')
            konfet -= bot
            #print(konfet)
        elif (12 < plauer < 19 and konfet <= 80) or (12 < plauer < 19 and konfet <= 60) or (18 < plauer < 29 and 60 <= konfet <= 200):
            bot = randint(9, 28)
            print(f'bot взял {bot} конфет')
            konfet -= bot
            #print(konfet)
        elif (19 < plauer < 29 or konfet <= 30) or (1 < plauer < 12 and konfet <= 35) or (1 < plauer < 12 and konfet <= 30):
            bot = randint(1, 1)
            print(f'bot взял {bot} конфет')
            konfet -= bot
            #print(konfet)
        else:
            bot = randint(1, 20)
            print(f'bot взял {bot} конфет')
            konfet -= bot
            #print(konfet)
        if konfet > 28:
            plauer = int(
                input(f'Ходит {Name}. Возьмите количество кофет не превышающее 28штук: \n'))
            while plauer <= 0 or plauer > 28:
                plauer = int(input(
                    f'{Name} вы ввели не вернау цифру, повторите ввод в диапазоне цифр от 1 до 28 включительно: \n '))
            konfet -= plauer
            #print(konfet)
            if konfet < 29:
                print('bot победил')
        else:
            print(f'{Name} победил(а)')

if x == 2:
    print('Первым ход осуществляет bot')              # Если первым ходит bot
    print()
    bot = randint(1, 28)
    print(f'bot взял {bot} конфет')
    konfet -= bot
    # print(konfet)
    print()
    while konfet > 28:
        plauer = int(
            input(f'Ходит {Name}. Возьмите количество кофет не превышающее 28штук: \n'))
        while plauer <= 0 or plauer > 28:
            plauer = int(input(
                f'{Name} вы ввели не вернау цифру, повторите ввод в диапазоне цифр от 1 до 28 включительно: \n '))
        konfet -= plauer
        # print(konfet)
        if (1 < plauer < 12 and 35 <= konfet <= 56) or (19 < plauer < 29 and 35 < konfet <= 56):
            bot = randint(1, 8)
            print(f'bot взял {bot} конфет')
            konfet -= bot
            # print(konfet)
        elif (12 < plauer < 19 and 56 < konfet <= 80) or (12 < plauer < 19 and 56 < konfet <= 60) or (18 < plauer < 29 and 60 <= konfet <= 200):
            bot = randint(9, 28)
            print(f'bot взял {bot} конфет')
            konfet -= bot
            # print(konfet)
        elif (10 < plauer < 29 or konfet <= 30) or (1 < plauer < 12 and konfet <= 35) or (1 < plauer < 12 and konfet <= 30):
            bot = randint(1, 1)
            print(f'bot взял {bot} конфет')
            konfet -= bot
            # print(konfet)

    if konfet > 28:
        print('bot победил')
    else:
        print(f'{Name} победил(а)')

 
