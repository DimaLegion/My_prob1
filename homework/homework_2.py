#Задача №2
#Определи, является ли год високосным?

a = input('Введите год:')
b = int(a)
if True==a.endswith('00'):
    print('Год не высокосный')
elif b%4==0:
    print('Год высокосный')
else:
   print('Год не высокосный')