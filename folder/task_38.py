# 38.	Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные:
# 'ываабв лповап абвцукв алоабвабв ываываыв'
# Входные данные: 
# 'лповап ываываыв'

#import string

text = 'ываабв лповап абвцукв алоабвабв ываываыв'
x = text.split(' ')
fragment = 'абв'
new_text = []
for i in x:
    if fragment not in i:
        new_text.append(i)
print(new_text)

