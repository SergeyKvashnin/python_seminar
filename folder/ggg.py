# Напишите программу, которая считывает последовательность 
# из 10 целых чисел и определяет является ли каждое из них четным или нет.

count = 0
n = 10
for _ in range(10):
    num = int(input())
    if num % 2 == 0:
        count += 1
        #print('YES')
    else:
        count
        #print('NO')
#print(count)
if n == count:
    print('YES')
else:
    print('NO')