# 32.    Задайте последовательность чисел. Напишите программу, которая выведет 
#           список неповторяющихся элементов исходной последовательности.


from enum import unique
from tokenize import Number
Number=[1,5,5,5,6,6,7,7,8,9,10]
unique_numbers = list(set(Number))
print(unique_numbers, end = '')

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

subs = [1, 3, 5, 4, 9, 14, 5, 1]
alone = []
for i in range (0, len(subs)):
    duplicate = 0
    for j in range(0, len(subs)):
        if i != j:
            if subs[i] == subs[j]:
                duplicate = 1
    if duplicate == 0:
        alone.append(subs[i])
print(alone)

# 32.	Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers=list(map(int,input('Введите последовательность чисел через пробел: ').split()))

print("Cписок неповторяющихся элементов исходной последовательности: ", list(set(numbers)))