import random
import string


def random_integer(num_digits=3):
    symb = string.digits
    return ''.join([random.choice(symb) for i in range(num_digits)])


def random_phone():
    return '+34' + str(random_integer(9))


def random_password(chars_count):
    symb = string.ascii_letters+string.ascii_lowercase
    return ''.join([random.choice(symb) for i in range(chars_count)])


def random_word(char_count):
    symb = string.ascii_letters
    return ''.join([random.choice(symb) for i in range(char_count)])


def random_text(word_count):
    return ' '.join([random_word(8) for i in range(word_count)])
