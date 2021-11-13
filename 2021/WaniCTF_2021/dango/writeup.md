# Writeup

以下のプログラムと出力結果が与えられる。

```py
import secrets
from functools import reduce

flag = b"FAKE{REDACTED}"
key = [secrets.token_bytes(len(flag)) for _ in range(3)]


def XOR(*X):
    xor = lambda A, B: bytes(x ^ y for x, y in zip(A, B))
    return reduce(xor, X)


ciphertext = XOR(flag, key[0])
A = XOR(key[0], key[1], key[2])
B = XOR(key[0], key[1])
C = XOR(key[1], key[2])

print(f"ciphertext : {ciphertext.hex()}")
print(f"A : {A.hex()}")
print(f"B : {B.hex()}")
print(f"C : {C.hex()}")
```

```
ciphertext : bd35b1c95ee9436db8fad5c3aa493660e606fa4dd7fe171aac75313c18ce5fcf86f0
A : cae61858ee8c7198632c652fd8416092eb165e2f847f0ebd80637ed0ffd96c6e0359
B : e6ed8bda14f67343d81830f0f2be3299a97b541db48cfa1873a13e8d774f1e243ce7
C : 319fe8d6cb01539bbcb9ef9f13663d8b6274c50b0ce578c94b7910b3ca785ccea8d4
```

`flag`は`ciphertext`と`key[0]`のXORをとれば分かるので、`key[0]`を求めたい。

`key[0]`を求めるためには`A`と`C`のXORをとればよい。

```py
from pwn import *

with open('cry-dango/output.txt') as f:
    ciphertext = bytes.fromhex(f.readline().split(' : ')[1].strip())
    A = bytes.fromhex(f.readline().split(' : ')[1].strip())
    B = bytes.fromhex(f.readline().split(' : ')[1].strip())
    C = bytes.fromhex(f.readline().split(' : ')[1].strip())

key0 = xor(A,C)
flag = xor(ciphertext,key0)
print(flag)
```

<!-- FLAG{dango_sankyodai_dango__-ooo-} -->
