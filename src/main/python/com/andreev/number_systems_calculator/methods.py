def change_system_to_10(s, from_system):
    result = 0
    for i in range(len(s)):
        if s[len(s) - 1 - i] == 'A':
            result += 10 * (from_system ** i)
        elif s[len(s) - 1 - i] == 'B':
            result += 11 * (from_system ** i)
        elif s[len(s) - 1 - i] == 'C':
            result += 12 * (from_system ** i)
        elif s[len(s) - 1 - i] == 'D':
            result += 13 * (from_system ** i)
        elif s[len(s) - 1 - i] == 'E':
            result += 14 * (from_system ** i)
        elif s[len(s) - 1 - i] == 'F':
            result += 15 * (from_system ** i)
        else:
            result += int(s[len(s) - 1 - i]) * (from_system ** i)
    return result


def change_system_from_10(s, to_system):
    n = int(s)
    result = ''
    while n > 0:
        if n % to_system == 10:
            result += 'A'
            n //= to_system
        elif n % to_system == 11:
            result += 'B'
            n //= to_system
        elif n % to_system == 12:
            result += 'C'
            n //= to_system
        elif n % to_system == 13:
            result += 'D'
            n //= to_system
        elif n % to_system == 14:
            result += 'E'
            n //= to_system
        elif n % to_system == 15:
            result += 'F'
            n //= to_system
        else:
            result += str(n % to_system)
            n //= to_system
    result = list(result)
    result.reverse()
    print('Результат:', *result, sep='')


def change_system_not_from_10_not_to_10(s, from_system, to_system):
    s_in_10 = str(change_system_to_10(s, from_system))
    change_system_from_10(s_in_10, to_system)
