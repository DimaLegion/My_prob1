N = int(input('Введите количество кандидатов:'))
col_fio = 0  # количество символов в ФИО
col_fio_2 = 0
col_dm = 0  # сумма цифр в дне и месяце рождения
k = 0  # Для первой (по позиции в слове) буквы фамилии определяется её номер в алфавите
odin = ''
while N != 0:
    f, i, o, d, m, y = input('Введите ФИО и ДМГ:').split(',')
    N = N - 1
    for kol in f, i, o:
        odin = odin + kol
    for kol_1 in odin:
        if odin.count(kol_1) == 1:
            col_fio = col_fio + 1
            print(col_fio,'col_fio',kol_1)
        if odin.count(kol_1) == 2:
            col_fio_2 = col_fio_2 + 1
            #print(col_fio, 'col_fio_2',kol_1)
    sum_col_fio = col_fio+int(col_fio_2/2)
    print(sum_col_fio)
    for kol in d, m:
        for kol_2 in kol:
            col_dm = col_dm + int(kol_2)
    print(col_dm)
    k = ord(f[0]) - 64
    print(k)  # Получение символа по его номеру из Unicode, только для больших букв
    itog = sum_col_fio + col_dm * 64 + k * 256
    print(itog)
    print(hex(itog))
    #отбрасываем
    hifr = str(hex(itog))
    print(hifr[-3:])

