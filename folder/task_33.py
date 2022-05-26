# 33.    Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в
#  файл многочлен степени k.
# Пример:
# 1.    k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import *
lst = list()
lst_1=list()
def rand():                     #метод создания рандомного числа
    r = randint(0, 101) 
    return r
def create_list(lst):              #метод создания списка случайных коэффициентов
    values = 3
    while values > 0:
        lst.append(rand())
        values= values - 1
    return lst
def polynominal(lst):              # метод создания строки многочлена
    n = lst[0], '*x^2 +', lst[1],'*x + ',lst[2], '=', 0
    n = str(n)
    n_str = n.replace(",","").replace("'","").replace("(","").replace(")","")
    return n_str
create_list(lst)
create_list(lst_1)
print(polynominal(lst))
print(polynominal(lst_1))

