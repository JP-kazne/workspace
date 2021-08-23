from Crypto.Util.number import *
import string

CHAR = string.printable
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase

check = [0x5f,0x40,0x5a,0x15,0x75,0x45,0x62,0x53,0x75,0x46,0x52,0x43,0x5f,0x75,0x50,0x52,0x75,0x5f,0x5c,0x4f]

flag = 'corctf{'
for i,c in enumerate(check):
    c ^= 42 # memfrob
    n = i << 2
    while not isPrime(n):
        n += 1
    if chr(c) not in LOWER+UPPER:
        flag += chr(c)
        continue
    for ch in LOWER+UPPER:
        if ch in LOWER:
            rotn = ord(LOWER[(ord(ch) - 0x61 + n) % 0x1a])
        elif ch in UPPER:
            rotn = ord(UPPER[(ord(ch) - 0x41 + n) % 0x1a])
        if rotn == c:
            flag += ch
            break
flag += '}'
print(flag)
