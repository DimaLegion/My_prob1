# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os
import os
os.chdir('..')
os.chdir('..')
os.chdir('..')
os.chdir('Desktop')
os.mkdir('Test') #создание папки Test
os.chdir('Test') #переход в папку для создание в ней файлов
f = open('test_1.txt', 'w') # создаем файлы
f.close()
f = open('test_2.txt', 'w')
f.close()
f = open('test_3.txt', 'w')
f.close()
os.rename('test_1.txt', 'rename_1.txt') #переименновываем их
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')
os.remove('rename_1.txt') #удаляем
os.remove('rename_2.txt')
os.remove('rename_3.txt')
os.chdir('..') #возращаемся в предыдущий раздел для удаления папки
os.rmdir('Test') #удаляем папку
