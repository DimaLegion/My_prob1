#Создай список, замени первый его элемент на [1, 2, 3]
#затем в конец списка добавь сумму элементов вложенного списка.

a = ['hello', 3, 4, 5]
print(a)
a[0]=[1, 2, 3]
print(a, ':замена первого элемента')
b = sum(a[0])
print(b, ':сумма первого элемента')
a.append(b)
print(a, ':список, добав. в конец суммы первого элемента')