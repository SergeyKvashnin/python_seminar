# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

import os
os.system('cls')

x = True 
y = False 
 
x1 = True
y1 = True
 
x2 = False
y2 = True
 
x3 = False
y3 = False 
 
if not (x or y) == (not x and not y) and not (x1 or y1) == (not x and not y) and not (x2 or y2) == (not x2 and not y2) and not (x3 or y3) == (not x3 and not y3):
    print('утверждение истина')
else: 
    print('утверждение ложь')