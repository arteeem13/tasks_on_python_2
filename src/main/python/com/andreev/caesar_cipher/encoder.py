from src.main.python.com.andreev.caesar_cipher.specifications import *


def delta(list_s, alphabet_lowercase, alphabet_uppercase, list_delta):
    for i in range(len(list_s)):
        count = 0
        for j in range(len(list_s[i])):
            if list_s[i][j] in alphabet_lowercase or list_s[i][j] in alphabet_uppercase:
                count += 1
        list_delta.append(count)
    return list_delta


def encoder(list_s, list_delta, size_alphabet, alphabet_lowercase, alphabet_uppercase, first_lowercase, last_lowercase,
            first_uppercase, last_uppercase):
    result = ''
    for i in range(len(list_s)):
        for j in range(len(list_s[i])):
            el = list_s[i][j]
            if list_s[i][j] in alphabet_lowercase:
                if ord(el) + list_delta[i] % size_alphabet > ord(last_lowercase):
                    result += chr(ord(first_lowercase) + (list_delta[i] - (ord(last_lowercase) - ord(el)) - 1))
                else:
                    result += chr(ord(el) + list_delta[i])
            elif list_s[i][j] in alphabet_uppercase:
                if ord(el) + list_delta[i] % size_alphabet > ord(last_uppercase):
                    result += chr(ord(first_uppercase) + (list_delta[i] - (ord(last_uppercase) - ord(el)) - 1))
                else:
                    result += chr(ord(el) + list_delta[i])
            else:
                result += el
        result += ' '

    print('Зашифрованное предложение:', result)


def latin_encoder_on_word_length():
    s_input = input('Введите предложение для шифрования на латинице: ')
    list_s = s_input.split()
    list_delta = list()
    list_delta = delta(list_s, latin_alphabet_lowercase, latin_alphabet_uppercase, list_delta)
    encoder(list_s, list_delta, size_latin_alphabet, latin_alphabet_lowercase, latin_alphabet_uppercase,
            latin_first_lowercase, latin_last_lowercase, latin_first_uppercase, latin_last_uppercase)


def cyrillic_encoder_on_word_length():
    s_input = input('Введите предложение для шифрования на кириллице: ')
    list_s = s_input.split()
    list_delta = list()
    list_delta = delta(list_s, cyrillic_alphabet_lowercase, cyrillic_alphabet_uppercase, list_delta)
    encoder(list_s, list_delta, size_cyrillic_alphabet, cyrillic_alphabet_lowercase, cyrillic_alphabet_uppercase,
            cyrillic_first_lowercase, cyrillic_last_lowercase, cyrillic_first_uppercase, cyrillic_last_uppercase)


def latin_encoder_on_digit():
    s_input = input('Введите предложение для шифрования на латинице: ')
    n_input = int(input('Введите шаг кодирования: '))
    list_s = s_input.split()
    list_delta = [n_input] * len(list_s)
    encoder(list_s, list_delta, size_latin_alphabet, latin_alphabet_lowercase, latin_alphabet_uppercase,
            latin_first_lowercase, latin_last_lowercase, latin_first_uppercase, latin_last_uppercase)


def cyrillic_encoder_on_digit():
    s_input = input('Введите предложение для шифрования на кириллице: ')
    n_input = int(input('Введите шаг кодирования: '))
    list_s = s_input.split()
    list_delta = [n_input] * len(list_s)
    encoder(list_s, list_delta, size_cyrillic_alphabet, cyrillic_alphabet_lowercase, cyrillic_alphabet_uppercase,
            cyrillic_first_lowercase, cyrillic_last_lowercase, cyrillic_first_uppercase, cyrillic_last_uppercase)
