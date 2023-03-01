a = float(input('Введите первое число: '))
b = input('Введите операцию +-*/: ' )
c = float(input('Введите второе число: '))

if b=='+':
    print(a+c)
elif b=='-':
    print(a-c)
elif b=='*':
    print(a*c)
else:
    print(a/c)