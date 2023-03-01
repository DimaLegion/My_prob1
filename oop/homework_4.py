# Два метода в классе, один принимает в себя либо строку, либо число.
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или
# равно длине слова, выводить все гласные, иначе согласные; если число то, произведение суммы
# чётных цифр на длину числа.
# Длину строки и числа искать во втором методе


class poisk:

    def __init__(self):
        self.vvod()

    def func_take(self):
        if ex.a.isdigit():
            return sum * ex.func_long()
        if ex.a.isalpha():
            if count * count_1 <= ex.func_long():
                return glas
            else:
                return sogl

    def vvod(self):
        self.a = input("Введите строку или число: ")

    def func_long(self):
        return len(self.a)


ex = poisk()
sum = 0
count = 0
count_1 = 0
b = 'аеёиоуыэюя'
с = 'бвгджзйклмнпрстфхцчшщ'
glas = ''
sogl = ''
if ex.a.isdigit():
    for i in ex.a:
        if int(i) % 2 == 0:
            sum += int(i)
    print(ex.func_take())
elif ex.a.isalpha():
    for i in ex.a:
        if i in b:
            count += 1
            glas += i
    for i in ex.a:
        if i in с:
            count_1 += 1
            sogl += i
    print(ex.func_take())
