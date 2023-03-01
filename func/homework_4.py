# Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
import random

a = []
for i in range(0, 10):
    c = random.randint(1, 100)
    a.append(c)
print(a)


def sp(b):
    if b == []:
        return 0
    else:
        return b[0] + sp(b[1:])


print(sp(a))
