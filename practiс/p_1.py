# С клавиатуры вводится текст,
# определить, сколько в нём гласных, а
# сколько согласных.
# В случае равенства вывести на экран
# все гласные буквы

str_ = input("Введите текст: ")
a = 'аеёиоуыэюя'
b = 0
c = 0
e = ''
for i in str_:
    if i in a:
        b+=1
        e+=i
    else:
        c+=1
if b == c:
    print(e)

print(b)
print(c)