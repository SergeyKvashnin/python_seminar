# 32.    Задайте последовательность чисел. Напишите программу, которая выведет 
#           список неповторяющихся элементов исходной последовательности.


from enum import unique
from tokenize import Number
Number=[1,5,5,5,6,6,7,7,8,9,10]
unique_numbers = list(set(Number))
print(unique_numbers, end = '')