# Создать рецепты для каждой из пицц:итальянская, пепперони. С возможность добавления пицц и их рецептов
pepper ={'пепперони': 'пицца-соус, пепперони, сыр моцарелла, базилик'}
italy = {'итальянская':'пицца-соус, пепперони, свежие шампиньоны, грудинка (свинина), маслины, сыр моцарелла, базилик'}
now_pizza = {} # создание новой пиццы
all_pizza = [pepper, italy]

print("1. Искать пиццу: ")
print("2. Создать новую пиццу:")
print("3. Вывести все пиццы:")
print("Для выхода нажмите n:")
pizza = int(input())
# while True:
if str(pizza) == 'n':
    print()        # break
elif pizza == 1:
    name = input("Введите название пиццы: ")
    if name == 'пепперони':
        print(pepper)
    if name == 'итальянская':
        print(italy)
        # break
elif pizza == 2:
    create_pizza = input("Введите название пиццы: ")
    all_pizza.append(create_pizza)
    create1_pizza = input("Введите ее состав:")
    now_pizza = {create_pizza: create1_pizza}
        # break
elif pizza == 3:
    for i in all_pizza:
        print(i)
        # break
