# Writeup

暗号文と平文のXORをとって鍵を計算する。

同じ鍵を再利用しているとのことなので、2つ目の暗号文も同じ鍵で復号できる。

```py
from pwn import *
from Crypto.Util.number import *

c1 = 0x4fd098298db95b7f1bc205b0a6d8ac15f1f821d72fbfa979d1c2148a24feaafdee8d3108e8ce29c3ce1291
p1 = b'hey let\'s rob the bank at midnight tonight!'
c2 = 0x41d9806ec1b55c78258703be87ac9e06edb7369133b1d67ac0960d8632cfb7f2e7974e0ff3c536c1871b

c1 = long_to_bytes(c1)
c2 = long_to_bytes(c2)

key = xor(c1, p1)
print(xor(c2, key))
```

<!-- MetaCTF{you're_better_than_steve!} -->
