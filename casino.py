# Казино. Числа от 1 до 10 и цвета от 1 до 2( 1 - красный, 2 - чёрный). У пользователя 5 попыток

import random

d = random.randint(1, 10)
e = random.randint(1, 2)
c = 0
while c < 5:
    a = int(input('Введите число от 1 до 10:'))
    b = int(input('Введите цвет 1 или 2(1-красный, 2-черный): '))
    c = c + 1
    if d == a and e == b:
        print(f'Вы угадали число и цвет {a},{b}')
        break
    elif d != a and e == b:
        print(f'Вы неугадали число, но угадали цвет {a},{b}')
        print(f'Правильная комбинация {d},{e}')
    elif d == a and e != b:
        print(f'Вы угадали число, но неугадали цвет {a},{b}')
        print(f'Правильная комбинация {d},{e}')
    else:
        print(f'Вы неугадали число и цвет {a},{b}')
else:
    print('Ваши попытки закончились!')
