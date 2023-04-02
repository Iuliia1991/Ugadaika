s = 'Hawnj pk swhg xabkna ukq nqj.'
new_s = ''
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2

for j in range(1, 26):
    for i in s:
        if i.isupper():
            ind = eng_upper_alphabet.rfind(i)
            new_s += eng_upper_alphabet[ind - j]
        elif i.islower():
            ind = eng_lower_alphabet.rfind(i)
            new_s += eng_lower_alphabet[ind - j]
        else:
            new_s += i

    print(new_s)
    new_s = ''