import sqlite3

conn = sqlite3.connect('name1.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
