inp = input('Введите строку: ')
str_vow = 'уеэоаыяию'
str_oth = 'йцкнгшщзхфвпрлджбтмсч'
flag_pair_low = 0
count_pairs_low = 0
flag_pair_up = 0
count_pairs_up = 0

for i in inp:
    if i.islower():
        flag_pair_low += 1
        if flag_pair_low == 2:
            flag_pair_low = 0
            count_pairs_low +=1
    else:
        flag_pair_low = 0

for i in inp:
    if i.isupper():
        flag_pair_up += 1
        if flag_pair_up == 2:
            flag_pair_up = 0
            count_pairs_up +=1
    else:
        flag_pair_up = 0

cnt_vow = 0
cnt_oth = 0
for x in inp.lower():
    if x in str_vow:
        cnt_vow += 1
    elif x in str_oth:
        cnt_oth += 1
print(f'Всего букв в слове: {len(inp)}, гласных: {cnt_vow} ,согласных: {cnt_oth}, '
                                        f'Пар нижнего регистра: {count_pairs_low} ,'
                                        f'пар верхнего регистра: {count_pairs_up}')