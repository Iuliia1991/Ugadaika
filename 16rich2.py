s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E','F']
num = 1000
cel = 0
ost = ''
while num >= 16:
    cel = num // 16
    ost += s[num % 16]
    num = cel
print(str(num) + ost[::-1])