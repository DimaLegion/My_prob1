# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями.

a = ['world', 'city', 3, 6, 'sun', 7]
b = 0
k = 0
c = ''
if isinstance(a, tuple):
    for i in a:
        print(f'Длина слова {i} равна:', len(i))
        b += len(i)
    print('Общая длина слов равна:', b)
elif isinstance(a, list):
    for i in a:
        c = str(i)
        if c.isalpha():
            print(f'Количество букв в слове {c} равно:', len(c))
        if c.isdigit():
            if int(c) % 2 != 0:
                k += 1
    print('Количество нечетных цифр равна:', k)
