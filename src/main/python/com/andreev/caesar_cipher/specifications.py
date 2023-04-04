latin_alphabet_lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
latin_alphabet_uppercase = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
size_latin_alphabet = 26
latin_first_lowercase, latin_last_lowercase = 'a', 'z'
latin_first_uppercase, latin_last_uppercase = 'A', 'Z'

cyrillic_alphabet_lowercase = [chr(i) for i in range(ord('а'), ord('я') + 1)]
cyrillic_alphabet_uppercase = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
cyrillic_first_lowercase, cyrillic_last_lowercase = 'а', 'я'
cyrillic_first_uppercase, cyrillic_last_uppercase = 'А', 'Я'
size_cyrillic_alphabet = 33


def delta(list_s, alphabet_lowercase, alphabet_uppercase, list_delta):
    for i in range(len(list_s)):
        count = 0
        for j in range(len(list_s[i])):
            if list_s[i][j] in alphabet_lowercase or list_s[i][j] in alphabet_uppercase:
                count += 1
        list_delta.append(count)
    print(list_delta)
    return list_delta
