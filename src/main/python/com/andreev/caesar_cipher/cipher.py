s_input = input('Введите предложение для шифрования на латинице: ')
list_s = s_input.split()
result = ''

a_z = [chr(i) for i in range(ord('a'), ord('z') + 1)]
A_Z = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

list_delta = list()
for i in range(len(list_s)):
    count = 0
    for j in range(len(list_s[i])):
        if list_s[i][j] in a_z or list_s[i][j] in A_Z:
            count += 1
    list_delta.append(count)

for i in range(len(list_s)):
    for j in range(len(list_s[i])):
        el = list_s[i][j]
        if list_s[i][j] in a_z:
            if ord(el) + list_delta[i] % 26 > ord('z'):
                result += chr(ord('a') + (list_delta[i] - (ord('z') - ord(el)) - 1))
            else:
                result += chr(ord(el) + list_delta[i])
        elif list_s[i][j] in A_Z:
            if ord(el) + list_delta[i] % 26 > ord('Z'):
                result += chr(ord('A') + (list_delta[i] - (ord('Z') - ord(el)) - 1))
            else:
                result += chr(ord(el) + list_delta[i])
        else:
            result += el
    result += ' '

print('Зашифрованное предложение:', result)
