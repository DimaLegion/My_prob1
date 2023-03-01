# Продемонстрируйте разные уровни доступа на примере любого класса

class Account:
    name = 'Bob'
    _balance = 10000
    __passport = 'USA'


a1 = Account()
print(a1.name)
print(a1._balance)
print(a1._Account__passport)

