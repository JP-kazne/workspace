import string
import re
from pwn import *

alpha = string.ascii_lowercase

def encrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            ret += alpha[(alpha.index(key[i]) + alpha.index(c)) % len(alpha)]
            i = (i + 1) % len(key)
        else:
            ret += c
    return ret

def decrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            ret += alpha[(alpha.index(key[i]) * (-1) + alpha.index(c)) % len(alpha)]
            i = (i + 1) % len(key)
        else:
            ret += c
    return ret

inner = alpha + "_"
noise = inner + "{}"

io = remote('challs.actf.co', 31333)

for _ in range(50):
    print(io.recvuntil(': '))
    msg = io.recvline().decode()
    guess = re.findall(r'(?=([a-z]{4}\{[^\{\}]{10,50}\}[a-z]{4}))', msg)

    for g in guess:
        _key = decrypt(g, 'actf')[:4]
        fleg = decrypt(g, _key)
        if fleg[-4:] == 'fleg':
            print(fleg[:-4])
            io.sendline(fleg[:-4])
            break
