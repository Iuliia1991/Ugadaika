eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

s = 'To be, or not to be, that is the question!'
k = 17
sh = ''
for c in s:
    if c.isalpha():
        if c in eng_upper_alphabet:
            x = eng_upper_alphabet.find(c)
            st = x + k
            if st > len(eng_upper_alphabet):
                st -= len(eng_upper_alphabet)
            sh += eng_upper_alphabet[st]

        elif c in eng_lower_alphabet:
            x = eng_lower_alphabet.find(c)
            st = x + k
            if st > len(eng_lower_alphabet):
                st -= len(eng_lower_alphabet)
            sh += eng_lower_alphabet[st]
    else:
        sh += c
print(sh)

