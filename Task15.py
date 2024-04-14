"""
15) Выведите на экран следующую пирамидку:
XX
XxxX
XxxxxX
XxxxxxxX
XxxxxxxxxX
Ваша пирамидка должна соблюдать регистр как в примере.
"""

num = -2
for i in range(5):
    num += 2

    row = 'X'  + 'x' * num + 'X'
    print(row)