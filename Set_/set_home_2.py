#Проверить, есть ли в последовательности чисел списка дубликаты.

a = [1, 2, 3, 5, 4, 5, 7]
b = set(a)
if len(a) == len(b):
    print('Список не имеет дубликатов')
else:
    print(f'Список имеет дубликаты ')

