# Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system('cls')
print([((-3)**i) for i in range(int(input('Введите число N: ')))])