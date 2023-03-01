# Написать функцию, которая определяет количество
# разрядов введенного целого числа

def func(n):
    b = 0
    while n > 0:
        n = n // 10
        b += 1
    return b


n = int(input())
print(func(n))
