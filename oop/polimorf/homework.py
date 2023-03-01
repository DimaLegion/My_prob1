# Придумайте свой примеры видов полиморфизма. Прикрепите скриншоты или файл с ними.

# class Del:
#
#     def start(self, a, b=None):
#         if b is not None:
#             if b != 0:
#                 print(a / b)
#             else:
#                 print(b)
#         else:
#             print(a)
#
#
# obj = Del()
# obj.start(10,5)

# 2 задача по теме полиморфизм

class Airplane:

    def __init__(self):
        self.fly = True
        print(f'Он летает:',self.fly)

    def info(self):
        print(f"Class name", Airplane.__name__)


class Plane(Airplane):

    def __init__(self):
        super().__init__()

    def info(self):
        print(f"Class name:", Plane.__name__)


def show_polymorphism():
    for item in [Airplane, Plane]:
        print('________')
        obj = item()
        obj.info()


show_polymorphism()
