sweet = {'торт': [('мука', 'яйца', 'сахар', 'ванилин'), 2.5, 10000],
         'пирожное': [('мука', 'яйца', 'сахар', 'масло сливочное'), 3.5, 1000],
         'маффин': [('мука', 'порошок какао', 'сахар тростниковый'), 4.5, 700]}

print('1.Описание')
print('2.Цена')
print('3.Количество')
print('4.Вся информация')
print('5.Покупка')
print('6.До свидания')

cost = 0
while True:
    a = int(input('Выберите из меню:'))
    if a == 1:
        b = input('Введите название:')
        print(sweet[b][0])
    elif a == 2:
        b = input('Введите название:')
        print('Цена за 100 грамм:', sweet[b][1])
    elif a == 3:
        b = input('Введите название:')
        print('Количество в граммах:', sweet[b][2])
    elif a == 4:
        for i in sweet.items():
            print(i)
        print(f'Цена выбранных товаров: {cost}.р')
    elif a == 5:
        while True:
            b = input('Введите название:')
            if b == 'n':
                break
            c = input('Введите количество которое хотите купить:')
            sweet[b][2] -= int(c)
            cost += sweet[b][1] * int(c)
    else:
        print('До свидания')
        break