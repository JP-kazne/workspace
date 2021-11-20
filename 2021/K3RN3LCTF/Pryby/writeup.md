# Writeup

以下のプログラムが与えられる。

```py
from Crypto.Util.number import bytes_to_long 
def f(n):
    q=[True]*(n + 1)
    r=2
    while r**2<=n:
        if q[r]:
            for i in range(r**2,n+1,r):q[i] = False
        r += 1
    return [p for p in range(2,n+1) if q[p]]
class G:
    def __init__(self, f):
        self.f = f
        self.state = 1
    def move(self):
        q=1
        for p in self.f:
            if self.state%p!=0:
                self.state=self.state*p//q
                return
            q*=p
flag = open('flag.txt','r').read().strip().encode()
flag=bytes_to_long(flag)
gen = G(f(pow(10,6)))
for _ in range(flag):gen.move()
print('enc =',gen.state)
# enc = 31101348141812078335833805605789286074261282187811930228543150731391596197753398457711668323158766354340973336627910072170464704090430596544129356812212375629361633100544710283538309695623654512578122336072914796577236081667423970014267246553110800667267853616970529812738203125516169205531952973978205310
```

ランダムな部分はなさそうなので、`b'\x01'`, `b'\x02'`を順に暗号化していき、規則性を探した。

```
0b1 2
0b10 3
0b11 6
0b100 5
0b101 10
0b110 15
0b111 30
0b1000 7
0b1001 14
0b1010 21
0b1011 42
0b1100 35
0b1101 70
0b1110 105
0b1111 210
0b10000 11
0b10001 22
0b10010 33
0b10011 66
0b10100 55
0b10101 110
0b10110 165
0b10111 330
0b11000 77
```

すると、ビットが立っている部分に対して素数の積をとっていることが分かった。

```
1 = 2
11 = 3 * 2
111 = 5 * 3 * 2
1111 = 7 * 5 * 3 * 2
``` 

`f(n)`で素数のリストを作成しているので活用して復号する。

```py
from Crypto.Util.number import *
def f(n):
    q=[True]*(n + 1)
    r=2
    while r**2<=n:
        if q[r]:
            for i in range(r**2,n+1,r):q[i] = False
        r += 1
    return [p for p in range(2,n+1) if q[p]]

enc = 31101348141812078335833805605789286074261282187811930228543150731391596197753398457711668323158766354340973336627910072170464704090430596544129356812212375629361633100544710283538309695623654512578122336072914796577236081667423970014267246553110800667267853616970529812738203125516169205531952973978205310
p_list = f(pow(10,6))
flag = 0
for i,p in enumerate(p_list):
    if enc%p == 0:
        flag += 2**i
print(long_to_bytes(flag))
```

<!-- flag{functi0n_h4cking_ftw!} -->
