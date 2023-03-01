# Создайте класс Example. В нём пропишите 3 (метода) функции. Две переменные
# задайте статически, две динамически.
# ❖ Первая функция: создайте переменную и выведите её
# Вторая функция: верните сумму 2-ух глобальных переменных
# Третья функция: верните результат возведения первой динамической переменной во вторую динамическую переменную
# Создайте объект класса.
# Напечатайте обе функции
# Напечатайте переменную a

class Example:
    a = 3
    b = 5

    def __init__(self, c, d):
        self.c = c
        self.d = d

    def func(self):
        self.f = 7
        print(self.f)

    def func_1(self):
        return self.a + self.b

    def func_2(self):
        return self.c ** self.d


object = Example(4, 6)
object.func()
print(object.func_1())
print(object.func_2())
print(object.a)
