# Обратный порядок цифр 

n = int(input())
while n > 0:
    print(n%10)
    n = n // 10
    

n = int(input())
while n != 0:
    print(n % 10, end ='')
    n = n // 10