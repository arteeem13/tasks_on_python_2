from src.main.python.com.andreev.guess_the_number_game.play import start_play

print('Добро пожаловать в числовую угадайку')
start_play()
question = input('Хотите сыграть заново? Если да, введите Y, если нет - N: ')
while question != 'N':
    if question == 'Y':
        start_play()
    else:
        question = input('Вы ввели неверное значение? Если хотите сыграть заново, введите Y, если нет - N: ')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
