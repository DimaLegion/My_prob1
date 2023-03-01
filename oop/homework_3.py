# Допишите по 2 динамических и статических свойства в класс с предыдущего задания.
# Продемонстрируйте их работу

class fish():
    # статические свойства
    default_color = 'white'
    default_teeth = 5000

    def __init__(self, color, teeth):
        # динамические свойства
        self.color = color
        self.teeth = teeth

    def data(self):
        print('белая акула весит от 680 до 1100 кг и достигает длины 4.8 метра')

    def subclass(self):
        print('акула относится к подклассу пластиножаберных')


shark = fish('blue', 4500)
print(shark.default_color)
print(shark.color)

# print(dir(fish))
#
# shark.data()
# shark.subclass()
