number = 20
running = True
while running:
    guess = int(input('Введите число: '))
    if guess == number:
        print('Поздравляю вы угадали число!')
        running = False
