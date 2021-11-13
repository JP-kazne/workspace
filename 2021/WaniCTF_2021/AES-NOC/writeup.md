# Writeup

以下のプログラムが与えられる。

```py
import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.strxor import strxor

from secret import flag


class AESNOC:
    def __init__(self, key: bytes, iv: bytes):
        self.iv = iv
        self.key = key
        self.block_size = AES.block_size

    def encrypt(self, plaintext: bytes):
        cipher = AES.new(self.key, AES.MODE_ECB)
        plaintext = pad(plaintext, self.block_size)
        P = [
            plaintext[i : i + self.block_size]
            for i in range(0, len(plaintext), self.block_size)
        ]
        C = []

        P_prev = self.iv
        for p in P:
            c = cipher.encrypt(p)
            C.append(strxor(c, P_prev))
            P_prev = p

        return b"".join(C)


def main():
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = AESNOC(key, iv)

    assert len(flag) == 49
    assert flag.startswith(b"FLAG{")
    assert flag.endswith(b"}")

    iv = iv.hex()
    print(f"{iv = }")
    while True:
        print("1. Get encrypted flag")
        print("2. Encrypt")
        choice = int(input("> "))
        if choice == 1:
            encrypted_flag = cipher.encrypt(flag).hex()
            print(f"{encrypted_flag = }")
        elif choice == 2:
            plaintext = input("Plaintext [hex] > ")
            plaintext = bytes.fromhex(plaintext)
            ciphertext = cipher.encrypt(plaintext).hex()
            print(f"{ciphertext = }")
        else:
            print("Bye")
            break


if __name__ == "__main__":
    main()
```

ECBで暗号化したものに対し、以下のようにXORを計算することで暗号文としている。

```
* = XOR

Plaintext               : ECB       : Ciphertext
--------------------------------------------------------
FLAG{xxxxxxxxxxx (P1)   : E1        : E1 * iv
xxxxxxxxxxxxxxxx (P2)   : E2        : E2 * P1
xxxxxxxxxxxxxxxx (P3)   : E3        : E3 * P2
}                (P4)   : E4        : E4 * P3
```

ここで、flagの長さが49でブロックサイズが16なので、 P4 は `}` とパディングのみの

```
7d0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f
```

であることが確定する。これを暗号化すると`E4 * iv`が得られる。

```
* = XOR

Plaintext               : ECB       : Ciphertext
--------------------------------------------------------
}                (P4)   : E4        : E4 * iv
```

すると、`iv`とのXORをとって`E4`が得られ、`E4`と`E4 * P3`のXORをとって`P3`が得られる。

これを繰り返すと、`P1 ~ P4`が分かるので、つなぎ合わせればフラグになる。

```
1.
encrypt P4 = E4 * iv 

iv * (E4 * iv) = E4

E4 * (E4 * P3) = P3

2.
encrypt P3 = E3 * iv

iv * (E3 * iv) = E3

E3 * (E3 * P2) = P2

3.
encrypt P2 = E2 * iv

iv * (E2 * iv) = E2

E2 * (E2 * P1) = P1
```

```py
from pwn import *
from Crypto.Util.number import *

io = remote('aesnoc.crypto.wanictf.org', 50000)

cuts = lambda s : s.strip().replace('\'','')
sep = lambda c : [c[i:i+32] for i in range(0, len(c), 32)]
hex_xor = lambda a,b : hex(bytes_to_long(xor(bytes.fromhex(a.zfill(32)), bytes.fromhex(b.zfill(32)))))[2:]

io.recvuntil('iv = ')
iv = cuts(io.recvline().decode())
io.sendline('1')
io.recvuntil('encrypted_flag = ')
c = cuts(io.recvline().decode())

C = sep(c)

def encrypt(s):
    io.sendline('2')
    io.sendline(s)
    io.recvuntil('ciphertext = ')
    return cuts(io.recvline().decode())[:32]

p4 = '7d' + '0f' * 15
c = encrypt(p4)
p3 = hex_xor(hex_xor(c,iv),C[3])
c = encrypt(p3)
p2 = hex_xor(hex_xor(c,iv),C[2])
c = encrypt(p2)
p1 = hex_xor(hex_xor(c,iv),C[1])

flag = ''.join([bytes.fromhex(p).decode() for p in [p1,p2,p3,p4[:2]]])
print(flag)
```

<!-- FLAG{Wh47_h4pp3n$_1f_y0u_kn0w_the_la5t_bl0ck___?} -->
