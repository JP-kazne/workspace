# Writeup

以下のプログラムとその出力結果が与えられる。

```py
from Crypto.Util.number import *
from flag import flag

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p*q

mid = len(flag) // 2

e = 65537

m1 = int.from_bytes(flag[:mid], byteorder='big')
m2 = int.from_bytes(flag[mid:], byteorder='big')

assert m1 < 2**256
assert m2 < 2**256

m = [[p,p,p,p], [0,m1,m1,m1], [0,0,m2,m2],[0,0,0,1]]

# add padding
for i in range(4):
    for j in range(4):
        m[i][j] *= getPrime(768)

m = matrix(Zmod(p*q), m)

c = m^e

print("n =", n)
print("e =", e)
print("c =", list(c))
```

RSA暗号のパラメータ ![n,e](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+n,e) と以下の行列 ![c](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c) の値が出力されている。 

![c = m^e = 
\begin{pmatrix}
p r_11 & p r_12 & p r_13 & p r_14\\
0 & m_1 r_22 & m_1 r_23 & m_1 r_24\\
0 & 0 & m_2 r_33 & m_2 r_34\\
0 & 0 & 0 & r_44\\
\end{pmatrix}
^e \mod n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c+%3D+m+%5Ee%3D+%0A%5Cbegin%7Bpmatrix%7D%0Ap+r_11+%26+p+r_12+%26+p+r_13+%26+p+r_14%5C%5C%0A0+%26+m_1+r_22+%26+m_1+r_23+%26+m_1+r_24%5C%5C%0A0+%26+0+%26+m_2+r_33+%26+m_2+r_34%5C%5C%0A0+%26+0+%26+0+%26+r_44%5C%5C%0A%5Cend%7Bpmatrix%7D%0A%5Ee+%5Cmod+n)

![r_n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+r_n)は異なるランダムな値であり、![m_1](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_1),![m_2](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_2)はそれぞれフラグの前半部分、後半部分になっている。

行列 ![c](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c) の対角成分について計算すると、以下のようになる。

![c = 
\begin{pmatrix}
(p r_11)^e & - & - & -\\
0 & (m_1 r_22)^e & - & -\\
0 & 0 & (m_2 r_33)^e & -\\
0 & 0 & 0 & (r_44)^e\\
\end{pmatrix}
\mod n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c+%3D+%0A%5Cbegin%7Bpmatrix%7D%0A%28p+r_11%29%5Ee+%26+-+%26+-+%26+-%5C%5C%0A0+%26+%28m_1+r_22%29%5Ee+%26+-+%26+-%5C%5C%0A0+%26+0+%26+%28m_2+r_33%29%5Ee+%26+-%5C%5C%0A0+%26+0+%26+0+%26+%28r_44%29%5Ee%5C%5C%0A%5Cend%7Bpmatrix%7D%0A%5Cmod+n)


![(p r_11)^e](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%28p+r_11%29%5Ee)と ![n = p q](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+n+%3D+p+q) はともに ![p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p) の倍数であるので、最大公約数を計算すると ![p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p) が得られる。

【解法１】

得られた ![p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p) から秘密鍵 ![d](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+d) を求めることができるので、![c^e](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c^d) を計算すると ![m](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m) がわかる。

すると、![m_1 r_22 , m_1 r_23](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_1+r_22+%2C+m_1+r_23) の最大公約数から ![m_1](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_1)  、![m_2 r_33 , m_2 r_34](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_2+r_33+%2C+m_2+r_34) の最大公約数から ![m_2](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_2) がわかるので、フラグを復号できる。

```py
from Crypto.Util.number import *

n, e, c = 0, 0, 0
exec(open('pppp/output.txt').read())

p = GCD(n, c[0][0]) # c[0][0] = (p*r)^e
q = n // p
assert p*q == n
d = int(pow(e, -1, (p-1)*(q-1)))

m = matrix(Zmod(n), c)^d

flag = long_to_bytes(GCD(int(m[1][1]),int(m[1][2])))
flag += long_to_bytes(GCD(int(m[2][2]),int(m[2][3])))

print(flag)
```

---

【解法２】

得られた ![p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p) から秘密鍵 ![d](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+d) を求めることができるので、対角成分から ![m_1 r_22 , m_2 r_33, r_44](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_1+r_22+%2C+m_2+r_33%2C+r_44) がわかる。

![r](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+r) が768ビットであり、![m \times r
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m+%5Ctimes+r%0A) は1024ビットを超えないことから、素因数分解すればよい。

![m_1 r_22](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_1+r_22) は Msieve を使って以下のように素因数分解することができた。

```
# p1: 2
# p2: 11
# p2: 11
# p3: 101
# prp11: 17733194681
# prp11: 21989360161
# prp21: 194838390862027996463
# prp231: 890941089701337639742923670629764992383197102649368033477055542426171609788212371754143394788213291456300216361551640449365841636339404366563906765128981689755176699342918904671528454362377482743831820969956624190146702130809843851
```

明らかに`prp231`の値が ![r](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+r) なので、残りの素数の積が平文である。

![m_2 r_33](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_2+r_33) は Msieve を使っても素因数分解することができなかった。

行列 ![c](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c) の 3行4列目を計算すると、
![m_2 r_34 \sum_{n=1}^{e} r_{44}^{n-1} (m_2 r_33)^{e-n}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_2+r_34+%5Csum_%7Bn%3D1%7D%5E%7Be%7D+r_%7B44%7D%5E%7Bn-1%7D+%28m_2+r_33%29%5E%7Be-n%7D)
となる。

総和の部分は既に分かっている値から計算できるので、mod n の逆元を掛けることにより、![m_2 r_34](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_2+r_34) がわかる。

![m_2 r_33 , m_2 r_34](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_2+r_33+%2C+m_2+r_34) の最大公約数から ![m_2](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+m_2) がわかるので、フラグを復号できる。

```py
from Crypto.Util.number import *

n, e, c = 0, 0, 0
exec(open('pppp/output.txt').read())

p = GCD(n, c[0][0]) # c[0][0] = (p*r)^e
q = n // p
assert p*q == n
d = int(pow(e, -1, (p-1)*(q-1)))

m1s = pow(c[1][1], d, n) # c[1][1] = (m1*s)^e
m2t = pow(c[2][2], d, n) # c[2][2] = (m2*t)^e
# print(m1s)
# print(m2t)

flag = b''
### factorize m1s in Msieve ###
# p1: 2
# p2: 11
# p2: 11
# p3: 101
# prp11: 17733194681
# prp11: 21989360161
# prp21: 194838390862027996463
# prp231: 890941089701337639742923670629764992383197102649368033477055542426171609788212371754143394788213291456300216361551640449365841636339404366563906765128981689755176699342918904671528454362377482743831820969956624190146702130809843851
flag += long_to_bytes(2*11*11*101*17733194681*21989360161*194838390862027996463)

### m2t can't factorize in Msieve ###
### So, find another solution ###
u = pow(c[3][3], d, n) # c[3][3] = u^e

expr = 0
for i in range(e):
    expr += (pow(u,i,n) * pow(m2t,(e-1)-i,n))%n
    expr %= n

m2v = (pow(expr, -1, n) * c[2][3]) % n # m2*t*expr = c[2][3]
flag += long_to_bytes(GCD(int(m2t),int(m2v)))

print(flag)
```

<!-- SECCON{C4n_y0u_prove_why_decryptable?} -->
