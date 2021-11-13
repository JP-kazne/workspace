# Writeup

以下のプログラムと出力結果が与えられる。

```py
flag = b"FAKE{REDACTED}"


def bytes_to_int(B: bytes):
    X = 0
    for b in B:
        X <<= 8
        X += b
    return X


print(bytes_to_int(flag))
```

```
19116989514623535769166210117786818367158332986915210065591753844573169066323884981321863605962664727709419615399694310104576887228581060509732286555123028133634836954522269304382229987197
```

出力結果はバイト文字列を数値に変換している。なので、元に戻すためには数値をバイト文字列にすればよい。

```py
from Crypto.Util.number import *

d = open('cry-fox/output.txt').read()
print(long_to_bytes(d))
```

<!-- FLAG{R1ng_d1n9_ding_d1ng_ding3ring3ding?__Wa_p@_pa_p@_pa_p@_pow?__or_konko-n?} -->
