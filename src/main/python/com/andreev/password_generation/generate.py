from random import *

digits = list('0123456789')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
punctuation = list('!#$%&*+-=?@^_')
special_punctuation = list('il1Lo0O')
chars = list()
password = list()

count_password = int(input('Количество паролей нужно сгенерировать: '))
length_password = int(input('Длина пароля (минимальное количество символов 4): '))
digits_in_pass = input('Включать ли цифры {} ? Y / N: '.format(''.join(digits)))
uppercase_in_pass = input('Включать ли прописные буквы {} ? Y / N: '.format(''.join(uppercase_letters)))
lowercase_in_pass = input('Включать ли строчные буквы {} ? Y / N: '.format(''.join(lowercase_letters)))
symbols_in_pass = input('Включать ли символы {} ? Y / N: '.format(''.join(punctuation)))
deleted_in_pass = input('Исключать ли неоднозначные символы {} ? Y / N: '.format(''.join(special_punctuation)))

if deleted_in_pass == 'Y':
    for i in range(len(special_punctuation)):
        c = special_punctuation[i]
        if c in digits:
            digits.remove(c)
        if c in uppercase_letters:
            uppercase_letters.remove(c)
        if c in lowercase_letters:
            lowercase_letters.remove(c)
        if c in punctuation:
            punctuation.remove(c)
if digits_in_pass == 'Y':
    chars.extend(digits)
    password.append(choice(digits))
if uppercase_in_pass == 'Y':
    chars.extend(uppercase_letters)
    password.append(choice(uppercase_letters))
if lowercase_in_pass == 'Y':
    chars.extend(lowercase_letters)
    password.append(choice(lowercase_letters))
if symbols_in_pass == 'Y':
    chars.extend(punctuation)
    password.append(choice(punctuation))

for _ in range(count_password):
    password.extend(sample(chars, length_password - len(password)))
    shuffle(password)
    print(*password, sep='')
