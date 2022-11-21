import random

counter, digit, answer = 0, 0, ''


def is_valid(a):
    for i in range(0, 10000):
        if i != a:
            return False
        else:
            return True


def game():
    global digit
    global counter
    global answer
    import os
    clear = lambda: os.system('cls')
    clear()
    print('Не знаю, зачем ты этого хочешь, но да ладно...')
    while True:
        n = input('Введи число, обозначающее правую границу для случайного выбора числа(максимум - 9999) \n')
        if n.isdigit() and 1 < int(n) <= 9999:
            digit = random.randint(1, int(n))
            break
        else:
            print('Прошу вас, введите любое целое число больше единицы и меньше 9999')
    print('Добро пожаловать в числовую угадайку')

    while True:
        print('Вводи любое целое число в диапазоне от 1 до', n, '\n')
        a = int(input())
        if is_valid(a):
            print('А может быть все-таки введем целое число от 1 до', n, '?')
        elif a > int(n):
            print('Число больше заданной границы')
        elif a < 0:
            print('Это число ниже допустимого, соблюдай границы ввода')
        elif int(a) < digit:
            print('Число меньше загаданного, попробуй еще разок')
            counter += 1
        elif int(a) > digit:
            print('Число больше загаданного, попробуй еще разок')
            counter += 1
        else:
            print('Ты угадал, молодец!')
            print('Попыток потребовалось:', counter)
            break


def ending():
    global answer
    while True:
        answer = input('Если хочешь "повеселиться" еще разок, введи "y", если нет - "n" \n')
        if answer == 'y':
            game()
        elif answer == 'n':
            print('Спасибо, что поиграл в числовую угадайку. Я еще вернусь...')
            break
        else:
            print('Некорректный символ!')


game()
ending()
