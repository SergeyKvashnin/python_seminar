# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
from ast import operator
from itertools import accumulate
import os
import random
import operator

os.system("cls")

print(*list(accumulate([i for i in range(1, int(input())+1)], operator.mul)))