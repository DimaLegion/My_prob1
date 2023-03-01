# Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в соответствующую таблицу, затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, если нечётное, то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице. Если меньше, то обновить 1 запись в первой таблице на «hello»

import sqlite3

conn = sqlite3.connect('z_4.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT) ''')  # слово ,
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')  # число
s = [3, 'dom', 4, 'green', 7]
h = 0
for i in s:
    if str(i).isalpha():
        h = len(i)  # длина слова
        cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', (i,))
        cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', (h,))
    if str(i).isdigit():
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', (i,))
    if str(i).isdigit():
        if i % 2 != 0:
            cursor.execute('''INSERT INTO tab_2 (col_1) VALUES ('нечетное')''')
cursor.execute('''SELECT col_1 FROM tab_2''')
w = cursor.fetchall()
r = len(w) #кол.записей
#conn.commit()
if r > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = 1''')
conn.commit()
cursor.execute('''SELECT col_1 FROM tab_1''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT col_1 FROM tab_2''')
k = cursor.fetchall()
print(k)
