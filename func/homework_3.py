# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000
# и возвращающую True, если оно простое, и False - иначе.

import random


def is_prime(a):
    k = 0
    if a == 2:
        return True, a
    if a == 1 or a == 0:
        return False, a
    for i in range(2, a + 1):
        if a % i == 0:
            k += 1
            if k == 2:
                return False, a
    else:
        return True, a


print(is_prime(a=random.randint(0, 1000)))
