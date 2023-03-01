# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция
counter = 0


def dek_func(fn):
    global counter
    fn()
    counter += 1
    print(f'Вызвана декорируемая функция {counter} раз')


def fun():
    print('Milan')


dek_func(fun)
dek_func(fun)
dek_func(fun)