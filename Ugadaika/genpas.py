import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
chars1 = ''

cntPw = input('Укажите количество паролей для генерации: ')
lenPw = input('Укажите длину одного пароля: ')
digOn = input('Включать ли цифры 0123456789? (y/n) ')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')
if digOn == 'y':
    chars += digits
if ABCon == 'y':
    chars += uppercase_letters
if abcOn == 'y':
    chars += lowercase_letters
if chOn == 'y':
    chars += punctuation
if excOn == 'y':
    for i in range(len(chars)):
        if chars[i] not in 'il1Lo0O':
            chars1 += chars[i]
        else:
            continue
if excOn == 'n':
    chars1 = chars

def generate_password(length, chars):
    pas = ''
    for i in range(int(length)):
        pas += random.choice(chars)
    return pas

for _ in range((int(cntPw))):
    print(generate_password(lenPw, chars1))



