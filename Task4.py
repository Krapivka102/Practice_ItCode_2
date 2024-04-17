# 4) Выведите количество слов в строке, не используя метод split()

a = (input('Введите строку: '))

in_word = False
word_count = 0

for char in a:
    if char == ' ':
        in_word = False
    elif not in_word:
        word_count += 1
        in_word = True

print(word_count)


# Вариант 2 тк урока по циклам еще не было:
count = a.count(" ")
print(count + 1)


