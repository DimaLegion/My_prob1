#Вводятся три целых числа. Определи какое из них наибольшее?

a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = int(input('Введите третье целое число: '))

if a>b and a>c:
        print(a)
elif b>a and b>c or b==c and b>a:
        print(b)
elif c>a and c>b:
        print(c)
else:
    print(a)