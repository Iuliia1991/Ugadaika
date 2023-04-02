# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
guess = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

while True:
    n = input()
    if is_valid(n) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        n = int(n)

    if n < guess:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif n > guess:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
