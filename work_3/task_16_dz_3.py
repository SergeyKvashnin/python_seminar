# Задать список из n чисел последовательности
#  (1+1n)n и вывести на экран их сумму

import os
os.system('cls')

from msilib import sequence
nums = [round((1 + 1 / x)**x, 5) for x in range (1, int(input('Введите число: ')) + 1)]
print((nums), round(sum(nums), 5), sep='\n')