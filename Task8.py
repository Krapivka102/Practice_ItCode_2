# 8) Объедините два списка в один список двумя способами.

ls1 = [1, 2, 3]
ls2 = ['q', 'w', 'e']

ls3 = ls1 + ls2

ls1.extend(ls2)

print(ls3)
print(ls1)