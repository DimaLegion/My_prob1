# Есть словарь песен группы Depeche Mode
# 1)Выведите общее время звучания всех песен.
# 2)Создайте список песен, время звучаниях которых больше 5 минут
# 3)Создайте новый словарь тех песен, в название которых состоит из одного слова
a = 0
c = ' '
spis_pesen = []
v = []
x = []
violator_songsdict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 5.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18, 'Clean': 5.68,
}
for name, time_song in violator_songsdict.items():
    a += time_song
    if time_song > 5:
        spis_pesen.append(name)
print('список песен, время звучаниях которых больше 5 минут:', spis_pesen)
for name, time_song in violator_songsdict.items():
    if not c in name:
        x.append(name)
        v.append(time_song)
one_word_song = dict(zip(x, v))
print('новый словарь тех песен, в название которых состоит из одного слова: ', one_word_song)
print('общее время звучания всех песен:', a)
