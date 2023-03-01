a = int(input('Введите число:'))
# a = 7
if a > 0:
    b = a + 4
    if b == 3:
        print('3')
    elif b > 0:
        print(b)
    else:
        print('hello')
elif a == 0:
    print('0')
elif a < 0:
    print('a<0')
else:
    print('else')

number = 23
guess = int(input('Введите целое число:'))
if guess == number:
    print('Поздравляю вы угадали,')
    print('Хотя и не выграли никакого приза!')
elif guess < number:
    print('Нет, загаданное число немного больше этого.')
else:
    print('Нет, загаданное число немного меньше этого.')
