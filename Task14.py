# 14) Вам дан произвольный двумерный список:
array = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55]
    ]
# Нужно выполнить его транспонирование.

rows = len(array)
cols = len(array[0])

trans_array = [[0 for i in range(rows)] for i in range(cols)]

for i in range(rows):
    for j in range(cols):
        trans_array[j][i] = array[i][j]

for i in trans_array:
    print(i)
