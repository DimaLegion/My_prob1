class Car:
    def start(self, a, b=None):
        if b is not None:
            print(a + b)
        else:
            print(a)


obj = Car()
obj.start(10,5)
