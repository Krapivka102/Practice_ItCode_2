# 9) Соедините два списка и отсортируйте их. Затем удалите повторяющиеся элементы.

ls1 = [7, 3, 8, 3, 7, 1, 2, 4, 5]
ls2 = [1, 2, 7, 4, 2, 7, 8, 0, 6]

ls1.extend(ls2)
ls1.sort()
print(list(set(ls1)))