eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

s = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
k = 25
sh = ''
for c in s:
    if c.isalpha():
        if c in eng_upper_alphabet:
            x = eng_upper_alphabet.find(c)
            st = x - k
            sh += eng_upper_alphabet[st]

        elif c in eng_lower_alphabet:
            x = eng_lower_alphabet.find(c)
            st = x - k
            sh += eng_lower_alphabet[st]
    else:
        sh += c
print(sh)
