# Вывести на экран числа от -N до N
import os
os.system('cls')

a = abs(int(input('Введите число: ')))

for i in range(-a, a):
    print(i, end=' ')

# Показать первую цифру дробной части числа
import os
os.system('cls')

n=20.454573
print(int(n*10)%10)