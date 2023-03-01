# Допишите несколько атрибутов в класс с прошлого задания, продемонстрируйте их работу

class fish():
    def data(self):
        print('белая акула весит от 680 до 1100 кг и достигает длины 4.8 метра')

    def subclass(self):
        print('акула относится к подклассу пластиножаберных')


shark = fish()
print(dir(fish))

shark.data()
shark.subclass()
