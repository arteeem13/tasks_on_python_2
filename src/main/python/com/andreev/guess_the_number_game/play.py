from random import *


def start_play():
    input_top_n = int(input('Нужно угадать целое положительное число в диапазоне от 1 до n включительно. '
                            'Введите целое число n больше 1: '))
    if input_top_n <= 1:
        input_top_n = int(input('Ошибка ввода. Введите целое число n больше 1: '))

    random_n = randint(1, input_top_n)
    flag_input_n = False
    attempts_number = 1

    input_n = int(input('Введите целое число от 1 до {} включительно: '.format(input_top_n)))

    def is_valid(input_number):
        if 1 <= input_number <= 100:
            return True
        else:
            return False

    while not flag_input_n:
        if is_valid(input_n):
            flag_input_n = True
        else:
            input_n = int(input('А может быть все-таки введем целое число от 1 до 100? '
                                'Введите целое число от 1 до 100 включительно: '))

    while input_n != random_n:
        if input_n > random_n:
            input_n = int(input('Ваше число больше загаданного, попробуйте еще разок: '))
            attempts_number += 1
        elif input_n < random_n:
            input_n = int(input('Ваше число меньше загаданного, попробуйте еще разок: '))
            attempts_number += 1

    if input_n == random_n:
        if attempts_number % 10 == 1 and attempts_number != 11:
            print('Вы угадали за {0} попытку, поздравляем!'.format(attempts_number))
        elif 2 <= attempts_number % 10 <= 4 and 5 > attempts_number > 14:
            print('Вы угадали за {0} попытку, поздравляем!'.format(attempts_number))
        else:
            print("Вы угадали за {0} попыток, поздравляем!".format(attempts_number))
