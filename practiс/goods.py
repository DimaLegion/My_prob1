
goods = {"Apple": [4.5, 10],
         "Orange": [6.2, 5],
         "Pineapple": [10.0, 1],
         "Mango": [7.5, 2],
         "Banana": [3.8, 10]}

cena = 0
while True:
    good = input("Введите название товара который хочете купить или нажмите n для выхода:")
    if good == 'n' or good not in goods:
        break
    kolich = int(input("Введите количество товара которого хотели бы купить:"))
    if kolich > goods[good][1]:
        print(f'в наличии количество товара:{goods[good][1]} меньше чем вы покупаете')
        continue
    cena += kolich*goods[good][0]
    goods[good][1] -= kolich
print('Цена:',cena)
for key, value in goods.items():
    print('фрукт:',key,'цена:',value[0],'количество:',value[1])
