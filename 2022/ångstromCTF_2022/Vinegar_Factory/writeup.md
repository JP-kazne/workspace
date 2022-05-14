# Writeup

以下の Python プログラムが与えられる。

```py
#!/usr/local/bin/python3

import string
import os
import random

with open("flag.txt", "r") as f:
    flag = f.read().strip()

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

inner = alpha + "_"
noise = inner + "{}"

print("Welcome to the vinegar factory! Solve some crypto, it'll be fun I swear!")

i = 0
while True:
    if i % 50 == 49:
        fleg = flag
    else:
        fleg = "actf{" + "".join(random.choices(inner, k=random.randint(10, 50))) + "}"
    start = "".join(random.choices(noise, k=random.randint(0, 2000)))
    end = "".join(random.choices(noise, k=random.randint(0, 2000)))
    key = "".join(random.choices(alpha, k=4))
    print(f"Challenge {i}: {start}{encrypt(fleg + 'fleg', key)}{end}")
    x = input("> ")
    if x != fleg:
        print("Nope! Better luck next time!")
        break
    i += 1
```

`encrypt`関数は、`key`の文字の index 文アルファベットをずらすという処理になっているので、`decrypt`するためには反対向きにずらせばよい。 

暗号文の中でランダムでないものを`encrypt`したものは、`actf{...}fleg`という文字列だけなので、これを頼りに復号を試す。

暗号文中に、`XXXX{...}YYYY` となるものを探し、`XXXX`をずらして`actf`になるような`key`を探す。

`YYYY`を`key`でずらして`fleg`となれば、復号完了である。

```py
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
```

<!-- actf{classical_crypto_is_not_the_best} -->
