# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов.
f = open("txt_3.txt", 'r')
a = f.readlines()
b = []
c = ''
k = 0
for i in a:
    i = i[:-1]
    b.append(i)
print(b)
for i in b:
    k += 1
    c = len(i.replace(' ', ''))
    print(f'{k}.Длина строки: {c}')
print('Количество строк: ', len(a))
f.close()
