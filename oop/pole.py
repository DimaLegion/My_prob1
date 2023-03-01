class Car:
    # статический
    default_color = 'grey'

    def __init__(self, color, weight):
        # динамический
        self.color = color
        self.weight = weight


car_new = Car('green', 200)
print(car_new.default_color)
print(car_new.color)
