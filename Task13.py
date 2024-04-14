# 13) Вам дано множество студентов:
students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}

# А также множество рабочих:
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

"""
Кто-то из них учится и работает одновременно.

Предстоит вывести в консоль:
•	Всех людей
•	Всех тех, кто одновременно учится и работает
•	Всех тех, кто только работает, но не учится
•	Всех тех, кто либо учится, либо работает, но не одновременно
Покажите по два способа достижения результата для каждого пункта.
"""

a1 = students | employees
a2 = students.union(employees)
print('Все люди:')
print(f'Способ 1: {a1}')
print(f'Способ 2: {a2}')

b1 = students & employees
b2 = students.intersection(employees)

print('Все люди, кто одновременно учится и работает:')
print(f'Способ 1: {b1}')
print(f'Способ 2: {b2}')

c1 = employees - students
c2 = employees.difference(students)
print('Все люди, кто только работает, но не учится:')
print(f'Способ 1: {c1}')
print(f'Способ 2: {c2}')

d1 = (students | employees) - b1
d2 = students.union(employees).difference(b1)
print('Все люди, кто либо учится, либо работает, но не одновременно:')
print(f'Способ 1: {d1}')
print(f'Способ 2: {d2}')
