#Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму
import random

a = ([random.randint(0,9) for i in range(10)])
print(a)
print(sum(a))

#Выведите статистику частности букв в кортеже
print('Задание 2:')
long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и',
 'и', 'и', 'т', 'т', 'а', 'и', 'и',
 'и', 'и', 'и', 'т', 'и')
b = long_word.count('т')
c = long_word.count('а')
d = long_word.count('и')
print(f'буква т: {b}, буква а: {c}, буква и: {d}')