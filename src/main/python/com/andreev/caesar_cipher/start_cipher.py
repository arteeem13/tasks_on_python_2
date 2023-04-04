from src.main.python.com.andreev.caesar_cipher.decoder import *
from src.main.python.com.andreev.caesar_cipher.encoder import *

action = int(input('Выберите действие:\n[1] Закодировать по длине слов на латинице\n[2] Закодировать по длине слов на '
                   'кириллице\n[3] Закодировать по шагу на латинице\n[4] Закодировать по шагу на кириллице\n'
                   '[5] Декодировать по длине слов на латинице\n[6] Декодировать по длине слов на кириллице\n'
                   '[7] Декодировать по шагу на латинице\n[8] Декодировать по шагу на кириллице\n'
                   'Для выхода введите любой другой символ\nВведите число выбранного пункта: '))

if action == 1:
    latin_encoder_on_word_length()
elif action == 2:
    cyrillic_encoder_on_word_length()
elif action == 3:
    latin_encoder_on_digit()
elif action == 4:
    cyrillic_encoder_on_digit()
elif action == 5:
    latin_decoder_on_word_length()
elif action == 6:
    cyrillic_decoder_on_word_length()
elif action == 7:
    latin_decoder_on_digit()
elif action == 8:
    cyrillic_decoder_on_digit()
