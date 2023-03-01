import sqlite3

conn = sqlite3.connect('name1.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
# Удаление записи из таблицы по id, по значению
cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

# Обновление данных в таблице
cursor.execute('''UPDATE tab_1 SET col_1 = 'dom' WHERE id = 2''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

# Вы также можете использовать функцию fetchone() для получения первого результата.
a = 'hello'
cursor.execute('''SELECT * FROM tab_1 WHERE col_1='hello' ''')
conn.commit()
k = cursor.fetchone()
print(k)

# Список всех записей отсориторованных относительно третьей колонки
cursor.execute('''SELECT * FROM tab_1 ORDER BY col_2 DESC''')
conn.commit()
k = cursor.fetchall()
print(k)

# В нашем случае, мы искали по всей таблице записи третьей колонки, которые начинаются с 7.
# Знак процента (%) является подстановочным оператором.
cursor.execute('''SELECT  * FROM tab_1 WHERE id LIKE '%2' ''')
conn.commit()
k = cursor.fetchall()
print(k)