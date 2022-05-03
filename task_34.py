# 34.    Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
from fileinput import close

f1 = open('file1.txt', 'r')     # открываем file1 

for line in f1:                 # считываем его по строкам 
    str1 = line
    #print(str1)                 # выводим что считали в file1
fi = close()                    # закрываем file1
                 
coef_1 = int(str1[0])           # числовые значения приравниваем к коэффицентам
coef_2 = int(str1[4])
coef_3 = int(str1[7])
#print(coef_1,coef_2,coef_3)

f2 = open('file2.txt', 'r')     # открываем file2

for line in f2:                 # считываем его по строкам 
    str2 = line
    #print(str2) 
fi = close()                    # закрываем file1


coef_1_1 = int(str2[0]+str2[1])           # числовые значения приравниваем к коэффицентам
coef_2_2 = int(str2[5]+str2[6])
coef_3_3 = int(str2[9]+str2[10])
#print(coef_1_1, coef_2_2, coef_3_3)

coef_1 = coef_1 + coef_1_1              # складываем коэффиценты 
coef_2 = coef_2 + coef_2_2
coef_3 = coef_3 + coef_3_3
#print(coef_1,coef_2,coef_3)

result = (f'{coef_1}ab + {coef_2}b +{coef_3}a = 0')     # закладываем весь многочлен в result
f3 = open('file3.txt', 'w')
f3.write(result)
f3.close()
print(result)


