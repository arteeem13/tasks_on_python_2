from src.main.python.com.andreev.number_systems_calculator.methods import *

question_1 = input('Выберете начальную систему счисления:\n[1] двоичная\n[2] восьмеричная\n[3] десятичная\n'
                   '[4] шестнадцатеричная\nВведите нужный пункт: ')
s = ''
system_in = 0
system_out = 0
if question_1 == '1':
    s = input('Введите число в двоичной системе счисления: ')
    system_in = 2
elif question_1 == '2':
    s = input('Введите число в восьмеричной системе счисления: ')
    system_in = 8
elif question_1 == '3':
    s = input('Введите число в десятичной системе счисления: ')
    system_in = 10
elif question_1 == '4':
    s = input('Введите число в шестнадцатеричной системе счисления: ')
    system_in = 16

question_2 = input('Выберете конечную систему счисления:\n[1] двоичная\n[2] восьмеричная\n[3] десятичная\n'
                   '[4] шестнадцатеричная\nВведите нужный пункт: ')
if question_2 == '1':
    system_out = 2
elif question_2 == '2':
    system_out = 8
elif question_2 == '3':
    system_out = 10
elif question_2 == '4':
    system_out = 16

if question_2 == '1':
    if question_1 == '3':
        change_system_from_10(s, system_out)
    else:
        change_system_not_from_10_not_to_10(s, system_in, system_out)
elif question_2 == '2':
    if question_1 == '3':
        change_system_from_10(s, system_out)
    else:
        change_system_not_from_10_not_to_10(s, system_in, system_out)
elif question_2 == '3':
    print('Результат:', change_system_to_10(s, system_out))
elif question_2 == '4':
    if question_1 == '3':
        change_system_from_10(s, system_out)
    else:
        change_system_not_from_10_not_to_10(s, system_in, system_out)
