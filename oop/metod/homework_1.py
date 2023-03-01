# Прикрепите файл с кодом, демонстрирующий работу разных видов методов класса

class My_Car():
    @staticmethod
    def drive():
        print('drive my car')


class Wife_Car(My_Car):
    pass


obj = My_Car()
obj.drive()
obj_1 = Wife_Car()
obj_1.drive()

print('@classmethod')


# classmethod

class My_Car1():
    A = 0

    def __init__(self):
        My_Car1.A = My_Car1.A + 1

    @classmethod
    def total_drive(cls):
        print('col_drive:', cls.A)


class Wife_Car1(My_Car1):
    A = 0

    def __init__(self):
        Wife_Car1.A = Wife_Car1.A + 1


a1 = My_Car1()
a2 = My_Car1()
a3 = Wife_Car1()
My_Car1.total_drive()
Wife_Car1.total_drive()
