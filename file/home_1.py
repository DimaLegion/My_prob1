# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел.
# Вывести в файл ‘output.txt’ их разность


f = open('input.txt', 'w')
f.write('4 2')
f.close()

f = open('input.txt')
c = 0
for line in f:
    b = line.split(' ')
    c = int(b[0])-int(b[1])
f.close()

with open('output.txt', 'w') as f:
    f.write(str(c))