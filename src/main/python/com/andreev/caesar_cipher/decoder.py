from src.main.python.com.andreev.caesar_cipher.encoder import *


def decoder(list_s, list_delta, size_alphabet, alphabet_lowercase, alphabet_uppercase, first_lowercase, last_lowercase,
            first_uppercase, last_uppercase):
    result = ''
    for i in range(len(list_s)):
        for j in range(len(list_s[i])):
            el = list_s[i][j]
            if el in alphabet_lowercase:
                if ord(el) - list_delta[i] % size_alphabet < ord(first_lowercase):
                    result += chr(ord(last_lowercase) - (list_delta[i] - (ord(el) - ord(first_lowercase)) - 1))
                else:
                    result += chr(ord(el) - list_delta[i])
            elif el in alphabet_uppercase:
                if ord(el) - list_delta[i] % size_alphabet < ord(first_uppercase):
                    result += chr(ord(last_uppercase) - (list_delta[i] - (ord(el) - ord(first_uppercase)) - 1))
                else:
                    result += chr(ord(el) - list_delta[i])
            else:
                result += el
        result += ' '

    print('Дешифрованное предложение:', result)


def latin_decoder_on_word_length():
    s_input = input('Введите предложение для дешифрования на латинице: ')
    list_s = s_input.split()
    list_delta = list()
    list_delta = delta(list_s, latin_alphabet_lowercase, latin_alphabet_uppercase, list_delta)
    decoder(list_s, list_delta, size_latin_alphabet, latin_alphabet_lowercase, latin_alphabet_uppercase,
            latin_first_lowercase, latin_last_lowercase, latin_first_uppercase, latin_last_uppercase)


def cyrillic_decoder_on_word_length():
    s_input = input('Введите предложение для дешифрования на кириллице: ')
    list_s = s_input.split()
    list_delta = list()
    list_delta = delta(list_s, cyrillic_alphabet_lowercase, cyrillic_alphabet_uppercase, list_delta)
    decoder(list_s, list_delta, size_cyrillic_alphabet, cyrillic_alphabet_lowercase, cyrillic_alphabet_uppercase,
            cyrillic_first_lowercase, cyrillic_last_lowercase, cyrillic_first_uppercase, cyrillic_last_uppercase)


def latin_decoder_on_digit():
    s_input = input('Введите предложение для дешифрования на латинице: ')
    n_input = abs(int(input('Введите шаг декодирования: ')))
    list_s = s_input.split()
    list_delta = [n_input] * len(list_s)
    decoder(list_s, list_delta, size_latin_alphabet, latin_alphabet_lowercase, latin_alphabet_uppercase,
            latin_first_lowercase, latin_last_lowercase, latin_first_uppercase, latin_last_uppercase)


def cyrillic_decoder_on_digit():
    s_input = input('Введите предложение для дешифрования на кириллице: ')
    n_input = abs(int(input('Введите шаг декодирования: ')))
    list_s = s_input.split()
    list_delta = [n_input] * len(list_s)
    decoder(list_s, list_delta, size_cyrillic_alphabet, cyrillic_alphabet_lowercase, cyrillic_alphabet_uppercase,
            cyrillic_first_lowercase, cyrillic_last_lowercase, cyrillic_first_uppercase, cyrillic_last_uppercase)
