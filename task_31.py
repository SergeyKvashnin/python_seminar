# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
#n = int(input('Введите множитель n: '))
#for i in range(1,101):
#    if i%n==0:
#        print(i)

#n = int(input('Введите число N:'))
#for i in range(1, n+1):
 #   if n%i == 0:
  #      print(f'множитель числа {n} = {i}')

n = int(input('Введите число: '))
n2 = []
while n!=1:
    if n%2==0:
        n=n//2
        n2.append(2)
    elif n%3==0:
        n=n//3
        n2.append(3)
    elif n%5==0:
        n=n//5
        n2.append(5)
    elif n%7==0:
         n=n//7
         n2.append(7)
    else:
         n2.append(n)
         n=1
print(n2)