# 10) Проверить, все ли числа в произвольной последовательности уникальны.

def isunique(s):
    if len(set(s)) == len(s):
        return 'Числа уникальны'
    else:
        return 'Числа не уникальны'


a1 = [1, 5, 8, 3, 6, 3, 1, 2, 0, 6]
a2 = [1, 0, 4, 7, 3, 8, 9, 2]
print(isunique(a1))
print(isunique(a2))
