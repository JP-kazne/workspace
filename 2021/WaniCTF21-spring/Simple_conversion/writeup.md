# Writeup

与えられたプログラムを読むと、バイト文字列をintに変換して出力している。

```py
from const import flag


def bytes_to_integer(x: bytes) -> int:
    x = int.from_bytes(x, byteorder="big")
    return x


print(bytes_to_integer(flag))
```

intを文字列に変換するプログラムを書くと、フラグが得られる。

```py
import os

c = open(os.path.dirname(__file__)+"/cry-simple-conversion/output.txt").read()
m = bytes.fromhex(hex(int(c))[2:])
print(m)
```

<!-- FLAG{7h1s_i5_h0w_we_c0nvert_m3ss@ges_1nt0_num63rs} -->
