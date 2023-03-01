# Файл содержит числа и буквы.
# Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию
# а потом слова по возрастанию их длинны.

f =open('text.txt', 'r')
a = f.readlines()
b = []
c = []
for i in a:
    i = i[:-1]
    if i.isalpha():
        b.append(i)
    elif i.isdigit():
        i = int(i)
        c.append(i)
b.sort()
c.sort()
print(c+b)
f.close()
