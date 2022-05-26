# from random import *


# konfet = 2021
# #x = randint(1,2)    # Рандом определяет кто ходит первым
# x=1
# print(x)


# if x == 1:          # Если первым ходит plauer_1  
#     plauer_1 = int(input('Первым ходит plauer_1. Возьмите количество конфет, не превышающее 28 штук: '))
#     while plauer_1 <=0 or plauer_1 > 28:
#         plauer_1 = int(input('введена не верная цифра. plauer_1, введите цифру в диапазоне от 1 до 28 включительно: '))
#     print(plauer_1)
#     konfet -= plauer_1
#     print(konfet)
#     while konfet > 28:
#         plauer_2 = int(input('Ходит plauer_2. Возьмите количество кофет не превышающее 28штук: '))
#         konfet -= plauer_2
#         print(konfet)
#         if konfet > 28:
#             plauer_1 = int(input('Ходит plauer_1. Возьмите количество кофет не превышающее 28штук: '))
#             konfet -= plauer_1
#             print(konfet)
#             if konfet < 29:
#                 print('plauer_2 победил')
#         else:
#             print('plauer_1 победил')

from random import *

konfet = 202
x = randint(1,2)    # Рандом определяет кто ходит первым
print(x)

if x == 1:          # Если первым ходит plauer_1  
    plauer = int(input('Первым ходит plauer. Возьмите количество конфет, не превышающее 28 штук: '))
    while plauer <=0 or plauer > 28:
        plauer = int(input('введена не верная цифра. plauer, введите цифру в диапазоне от 1 до 28 включительно: '))
    konfet -= plauer
    print(konfet)
    while konfet > 28:
        if (1< plauer <12 and 35 <= konfet <= 56) or (19< plauer <29 and 35 < konfet <= 56):
            bot = randint(1,8)
            print(bot)
            konfet -= bot
            print(konfet)
        elif (12 < plauer < 19 and konfet <= 80) or (12 < plauer < 19 and konfet <= 60) or (18 < plauer < 29 and 60 <= konfet <= 200):
            bot = randint(9,28)
            print(bot)
            konfet -= bot
            print(konfet)
        elif (19 < plauer < 29 or konfet <= 30) or (1< plauer <12 and konfet <= 35) or (1< plauer <12 and konfet <= 30):
            bot = randint(1,1)
            print(bot)
            konfet -= bot
            print(konfet)
        else:
            bot = randint(1,20)
            print(bot)
            konfet -= bot
            print(konfet)
        if konfet > 28:
            plauer = int(input('Ходит plauer. Возьмите количество кофет не превышающее 28штук: '))
            while plauer <=0 or plauer > 28:
                plauer = int(input('введена не верная цифра. plauer, введите цифру в диапазоне от 1 до 28 включительно: '))
            konfet -= plauer
            print(konfet)
            if konfet < 29:
                print('bot победил')
        else:
            print('plauer победил')
