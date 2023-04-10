num = 513
cel = 0
ost = ''
while num >= 2:
    cel = num // 2
    ost += str(num % 2)
    num = cel
print(str(num) + ost[::-1])