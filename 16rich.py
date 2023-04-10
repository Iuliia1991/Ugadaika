def from_hex_to_dec(num):
    result = 0
    count = len(num)
    for i in num:
        count -= 1
        if i.isdigit():
            result += int(i) * (16 ** count)
        else:
            result += (ord(i) - 55) * (16 ** count)
    return result

print(from_hex_to_dec(input('Введите число: ')))