# Writeup

以下のプログラムと出力結果が与えられる。

```py
def encrypt(msg, f):
    return ''.join(chr(f.substitute(c)) for c in msg)

P.<x> = PolynomialRing(ZZ)
f = 13*x^2 + 3*x + 7

FLAG = open('./flag.txt', 'rb').read().strip()

enc = encrypt(FLAG, f)
print(enc)
```

```
𖿫𖝓玲𰆽𪃵𢙿疗𫢋𥆛🴃䶹𬑽蒵𜭱𫢋𪃵蒵🴃𜭱𩕑疗𪲳𜭱窇蒵𱫳
```

Substitutionとのことなので、全文字列に対して対応表を作り、復号化した。

```py
import string

def encrypt(msg, f):
    return ''.join(chr(f.substitute(c)) for c in msg)

P.<x> = PolynomialRing(ZZ)
f = 13*x^2 + 3*x + 7

CHAR = string.printable
enc_dict = {}
for c in CHAR:
    enc_dict[str(encrypt(c.encode(), f))] = c

enc = open('output.txt', 'r').read().strip()
FLAG = ''
for e in enc:
    FLAG += enc_dict[e]
print(FLAG)
```

<!-- DUCTF{sh0uld'v3_us3d_r0t_13} -->
