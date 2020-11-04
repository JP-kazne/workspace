digest = [10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]
char = 'CSR{'

i = 0
for d in digest:
    x = chr(d ^ ord(char[i]))
    char += x
    i += 1

print(char)