# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.

f = open('text_16.txt', 'r', encoding='utf-8')
a = []
c = 0
for i in f:
    i = i[:-1]
    a.append(i)
print(a)
for str in a:
    for w in str:
        if w.isdigit():
            b = int(w)
            c += b
            if b < 3:
                print(str)
print('Средний бал по классу:', c / len(a))
