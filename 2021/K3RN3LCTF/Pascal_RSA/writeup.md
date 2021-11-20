# Writeup

以下のプログラムと出力結果が与えられる。

```py
triangle =[[1]]
flag = open('flag.txt','rb').read()

from Crypto.Util.number import getPrime,bytes_to_long
from math import gcd
p = getPrime(20)
while len(triangle[-1]) <= p:
    r = [1]
    for i in range(len(triangle[-1]) - 1):
        r.append(triangle[-1][i] + triangle[-1][i+1])
    r.append(1)
    triangle.append(r)
code = ''
for x in triangle[-1]:
    code+=str(x%2)
d = int(code,2)
while True:
    P = getPrime(512)
    Q = getPrime(512)
    if gcd(d, (P-1)*(Q-1)) == 1:
        N = P*Q
        e = pow(d,-1,(P-1)*(Q-1))
        break
enc = pow(bytes_to_long(flag), e, N)
file = open('challenge.txt','w')
file.write(f'p = {p}\nenc = {enc}\nN = {N}')
```

```
p = 751921
enc = 9820620269072860401665805101881284961421302475382405373888746780467409082575009633494008131637326951607592072546997831382261451919226781535697132306297667495663005072695351430953630099751335020192098397722937812151774786232707555386479774460529133941848677746581256792960571286418291329780280128419358700449
N = 84317137476812805534382776304205215410373527909056058618583365618383741423290821410270929574317899945862949829480082811084554009265439540307568537940249227388935154641779863441301292378975855625325375299980291629608995049742243591901547177853086110999523167557589597375590016312480342995048934488540440868447
```

パスカルの三角形を2進数で表現した時の値をRSA暗号の`d`にしている。

`p = 751921`のときの`d`を求めて、RSA暗号を復号する。

```
例)
p:             d
-----------------
0:     1     = 1
1:    1 1    = 3
2:   1 0 1   = 5
3:  1 1 1 1  = 15
4: 1 0 0 0 1 = 17
```

この`1,3,5,15,17,...`という数列は`a(n+1) = a(n) XOR 2*a(n)`で計算できる。

* https://oeis.org/A001317

以下のプログラムを実行してフラグが得られた。

```py
from Crypto.Util.number import *
from tqdm import tqdm

exec(open('challenge.txt').read())

d = 1
for i in tqdm(range(p)):
    d = d ^ 2*d

m = pow(enc, d, N)
print(long_to_bytes(m))
```

<!-- flag{1ts_ch00se_a11_a10ng??} -->
