eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = input()
s = n
for q in s:
    if q in '!#$%&*''""+-=?@^_.,':
        s = s.replace(q, '')
y = [len(i) for i in s.split()]
count = 0
word = ''
for c in n:
    if c == ' ':
        count += 1
        word += c
    elif c.isalpha():
        if c in eng_upper_alphabet:
            x = eng_upper_alphabet.find(c)
            st = x + y[count]
            if st > len(eng_upper_alphabet):
                st -= len(eng_upper_alphabet)
            word += eng_upper_alphabet[st]

        elif c in eng_lower_alphabet:
            x = eng_lower_alphabet.find(c)
            st = x + y[count]
            if st >= len(eng_lower_alphabet):
                st -= len(eng_lower_alphabet)
            word += eng_lower_alphabet[st]
    else:
        word += c
print(word)
