# Задача№1
# Значениями словаря могут быть и списки. Создайте словарь с ключами BMW, Tesla и списками из
# 3х моделей в качестве значений. Выведите первое и последнее значения каждого из ключей.

car = {'BMW': ['m2', 'm3', 'm5'], 'Tesla': ['s', 'x', 'y']}
print(car['BMW'][0], car['BMW'][2], car['Tesla'][0], car['Tesla'][2])

# Задача№2
# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

import math

b = []
a = {'1': 1, '2': 2, '3': 3, '4': 4}
for key, values in a.items():
    b.append(values)
print(math.prod(b))
