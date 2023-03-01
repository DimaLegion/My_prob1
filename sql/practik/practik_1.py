# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без учёта id
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД

import sqlite3
import random

conn = sqlite3.connect('z_2.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,col_2 INTEGER) ''')
a = random.randint(0, 9)
b = random.randint(0, 9)
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (a, b))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

cursor.execute('''SELECT col_1,col_2 FROM tab_1''')
c = cursor.fetchall()
print(c)
sum = 0
for i in c:
    for j in i:
        sum += j
print(sum)
print(sum / (len(c) * 2))
if sum > len(c):
    cursor.execute('''DELETE FROM tab_1 WHERE id=4''')
    conn.commit()
cursor.execute('''SELECT col_1,col_2 FROM tab_1''')
c = cursor.fetchall()
print(c)
