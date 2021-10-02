# Writeup

以下のスクリプトと出力結果が与えられる。

```py
from Crypto.Util.number import *

with open('flag.txt','rb') as g:
    flag = g.read().strip()

with open('nums.txt','r') as f:
	s=f.read().strip().split()
	a=int(s[0])
	b=int(s[1])
	c=int(s[2])


e=65537
n=a**3+b**3-34*c**3
m=bytes_to_long(flag)
ct=pow(m,e,n)


print ("n: ",n)
print ("e: ",e)
print ("ct: ",ct)
```

```
n:  57436275279999211772332390260389123467061581271245121044959385707165571981686310741298519009630482399016808156120999964
e:  65537
ct:  25287942932936198887822866306739577372124406139134641253461396979278534624726135258660588590323101498005293149770225633
```

RSA暗号の問題で、`n`がそこまで大きくないので、FactorDBで因数分解することができた。あとは、`phi(n)`を求めて復号化する。

```py
from factordb.factordb import FactorDB
from Crypto.Util.number import *

f = open('Not_Baby/out.txt', 'r').read().replace(':','=')
n, e, ct = 0, 0, 0
exec(f)

factor = FactorDB(n)
factor.connect()
factor = factor.get_factor_list()

phi = 1
for fc in factor:
    phi *= (fc-1)
d = pow(e,-1,phi)
m = pow(ct,d,n)
print(long_to_bytes(m))
```

<!-- flag{f4ct0ring_s0000oo00000o00_h4rd} -->
