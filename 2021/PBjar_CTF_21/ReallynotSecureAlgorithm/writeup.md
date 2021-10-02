# Writeup

以下のスクリプトと出力結果が与えられる。

```py
from Crypto.Util.number import *
with open('flag.txt','rb') as f:
    flag = f.read().strip()
e=65537
p=getPrime(128)
q=getPrime(128)
n=p*q
m=bytes_to_long(flag)
ct=pow(m,e,n)


print (p)
print (q)
print (e)
print (ct)
```

```
194522226411154500868209046072773892801
288543888189520095825105581859098503663
65537
2680665419605434578386620658057993903866911471752759293737529277281335077856
```

RSA暗号で`p,q`が分かっているので、`d`を計算して復号化すればよい。

```py
from Crypto.Util.number import *

f = open('ReallynotSecureAlgorithm/out.txt', 'r').read().splitlines()
[p, q, e, ct] = list(map(int, f))

d = pow(e, -1, (p-1)*(q-1))
m = pow(ct, d, p*q)
print(long_to_bytes(m))
```

<!-- flag{n0t_to0_h4rd_rIt3_19290453} -->
