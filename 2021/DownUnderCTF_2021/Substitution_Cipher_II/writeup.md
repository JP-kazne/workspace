# Writeup

以下のプログラムと出力結果が与えられる。

```py
from string import ascii_lowercase, digits
CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits
n = len(CHARSET)

def encrypt(msg, f):
    ct = ''
    for c in msg:
        ct += CHARSET[f.substitute(CHARSET.index(c))]
    return ct

P.<x> = PolynomialRing(GF(n))
f = P.random_element(6)

FLAG = open('./flag.txt', 'r').read().strip()

enc = encrypt(FLAG, f)
print(enc)
```

```
Ujyw5dnFofaou0au3nx3Cn84
```

ランダムな6次の関数で`substitute`が行われている。

```
f = a0*x^6 + a1*x^5 + a2*x^4 + a3*x^3 + a4*x^2 + a5*x + a6
```

フラグフォーマットの`DUCTF{}`がどの文字に置換されているかはわかるので、`f(x=0)`から`f(x=6)`を計算し、連立方程式を解けば`a0`から`a6`を求めることができる。

```py
from string import ascii_lowercase, digits
CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits
n = len(CHARSET)

def encrypt(msg, f):
    ct = ''
    for c in msg:
        ct += CHARSET[f.substitute(CHARSET.index(c))]
    return ct

P.<x> = PolynomialRing(GF(n))
enc = open('output.txt', 'r').read().strip()
# f = P.random_element(6)
# f = a0*x^6 + a1*x^5 + a2*x^4 + a3*x^3 + a4*x^2 + a5*x + a6

mat = []
for i in range(7):
    mat.append([i^6, i^5, i^4, i^3, i^2, i^1, i^0])    
M = Matrix(P, mat)
vec = [CHARSET.index(enc[i]) for i in range(6)]
vec.append(CHARSET.index(enc[-1]))
b = vector(P, vec)
solve = M.solve_right(b)

f = solve[0]*x^6 + solve[1]*x^5 + solve[2]*x^4 + solve[3]*x^3 + solve[4]*x^2 + solve[5]*x + solve[6]

enc_dict = {}
for c in CHARSET:
    enc_dict[c] = encrypt(c, f)

FLAG = ''
for e in enc:
    tmp = ''
    for key, value in enc_dict.items():
        if value == e:
            tmp += key
    if len(tmp) == 1:
        FLAG += tmp
    else:
        FLAG += '[' + tmp + ']'
print(FLAG)
```

置換結果が1対1対応でないものがあるので、フォーマットやleetの意味が通るように選択する。

```
D[U!]C[Tt]F{go0d_0l'_l4gr4[fnp]g[38]}
```

```
DUCTF{go0d_0l'_l4gr4ng3}
```

<!-- DUCTF{go0d_0l'_l4gr4ng3} -->
