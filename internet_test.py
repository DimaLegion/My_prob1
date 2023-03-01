#Даны списки:
#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(list(set(a) & set(b)))

#Отсортируйте словарь по значению в порядке возрастания и убывания.
import operator
a = {'1': 1, '2': 3, '3': 2, '4': 4}
# result = dict(sorted(a.items(), key=operator.itemgetter(1)))
# print(result)
# a = list(a.values())
# a.sort()
# print(a)
# a.reverse()
# print(a)

#Напишите программу для слияния нескольких словарей в один.

# a = {1: 'hello', 2: 'world'}
# b = {5: 'fish', 4: 'tynec'}
# print(a | b)

#Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(result)

#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12)
#и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

# season = int(input("Введите номер месяца: "))
# if season == 12 or season == 1 or season == 2:
#     print("Зима")
# if season == 3 or season == 4 or season == 5:
#     print("Весна")
# if season == 6 or season == 7 or season == 8:
#     print("Лето")
# if season == 9 or season == 10 or season == 11:
#     print("Осень")