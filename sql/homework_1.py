#Домашнее задание

#1.Сформулируйте SQL запрос для создания таблицы book. Структура таблицы book:
#2.Занесите новую строку в таблицуbook
#3.Выбрать информацию о всех книгах из таблицы book.

import sqlite3

conn = sqlite3.connect("h_1.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book(book_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(50), author VARCHAR(30), price DECIMAL(8, 2), amount INT)''' )
cursor.execute('''INSERT INTO book(title, author, price, amount) VALUES ('Гарри Поттер и узник Азкабана', 'Джоан Роулинг', '32,00', '1')''')
cursor.execute('''INSERT INTO book(title, author, price, amount) VALUES ('Десять негритят', 'Агата Кристи', '11,84', '1')''')
cursor.execute('''INSERT INTO book(title, author, price, amount) VALUES ('Триумфальная арка', 'Эрих Мария Ремарк', '16,00', '1')''')
conn.commit()
cursor.execute('''SELECT*FROM book''')
k = cursor.fetchall()
print(k)
for i in k:
    i = list(i)
    h = 0
    print(' '.join(str(h) for h in i))