# Writeup

以下のプログラムが与えられる。

```py
from Crypto.Util.number import bytes_to_long, getStrongPrime
from random import randrange
from secret import flag

LIMIT = 64

def gen():
	p = getStrongPrime(512)
	g = randrange(1, p)
	return g, p

def main():
	g, p = gen()
	print("g:", str(g))
	print("p:", str(p))
	x = bytes_to_long(flag)
	enc = pow(g, x, p)
	print("encrypted flag:", str(enc))
	ctr = 0
	while ctr < LIMIT:
		try:
			div = int(input("give me a number> "))
			print(pow(g, x // div, p))
			ctr += 1
		except:
			print("whoops..")
			return
	print("no more tries left... bye")

main()	
```

`g`, `p` , ![g^x \mod p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+g%5Ex+%5Cmod+p) , 任意の`d`に対して![g^{\frac{x}{d}} \mod p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+g%5E%7B%5Cfrac%7Bx%7D%7Bd%7D%7D+%5Cmod+p)が分かるという条件で、`x`の値を求めればよい。

次のような手順で、`x`の最上位ビットから1ビットずつ求めていく。

```
例) x = 25 = 0b11001 
```

1. `x` のビット数を求める
    
    `d = 2^y` としたとき、![g^{\frac{x}{d}} \mod p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+g%5E%7B%5Cfrac%7Bx%7D%7Bd%7D%7D+%5Cmod+p)が1となるような`y`が`x`のビット数になる。

    ``` 
    g^(25/2*5) = g^0 = 1 mod p
    ```

2. 最上位ビットから順に`2^y`で割っていく。結果が`g`の偶数乗ならば`0`, 奇数乗ならば`1`を記憶していくと`x`が復元できる。

    ```
    g^(25/2*4) = g^1 ≒ g^(0*2) mod p  ... 1
    g^(25/2*3) = g^3 ≒ g^(1*2) mod p ... 11
    g^(25/2*2) = g^6 = g^(3*2) mod p ... 110
    g^(25/2*1) = g^12 = g^(6*2) mod p ... 1100
    g^(25/2*0) = g^25 ≒ g^(12*2) mod p ... 11001
    ```

以下のプログラムを実行し、フラグが得られた。

```py
from pwn import *
from tqdm import tqdm
from Crypto.Util.number import *

LIMIT = 64
bit_length = 1
# bit_length = 511
enc_bit = ''

# find bit length of flag
def connection():
    io = remote('crypto.be.ax', 6000)
    io.recvuntil('g:')
    g = int(io.recvline().decode('utf-8'))
    io.recvuntil('p:')
    p = int(io.recvline().decode('utf-8'))
    io.recvuntil('encrypted flag:')
    enc = int(io.recvline().decode('utf-8'))
    return io,g,p,enc

found = False
while True:
    io,g,p,enc = connection()
    for _ in tqdm(range(LIMIT)):
        io.recvuntil('give me a number> ')
        io.sendline(str(1 << bit_length))
        enc_div = int(io.recvline().decode('utf-8'))
        if pow(enc_div, 1 << bit_length, p) == pow(g, 0, p):
            found = True
            break
        bit_length += 1
    io.close()
    if found:
        break

# determine MSB of flag
exp = 1
for bl in tqdm(range(bit_length-1,0,-1)):
    if (bit_length - (bl+1)) % LIMIT == 0:
        io,g,p,enc = connection()

    io.recvuntil('give me a number> ')
    io.sendline(str(1 << bl))
    enc_div = int(io.recvline().decode('utf-8'))
    if enc_div == pow(g,exp,p):
        pass
    else:
        exp += 1
    exp = exp << 1
print(long_to_bytes(exp))
```

（後から気づいたが、![g^{\frac{x}{d}} \mod p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+g%5E%7B%5Cfrac%7Bx%7D%7Bd%7D%7D+%5Cmod+p)が偶数乗かどうかの判定は、平方剰余かどうかの判定を行えばよい。）

<!-- corctf{qu4drat1c_r3s1due_0r_n0t_1s_7h3_qu3st1on8852042051e57492} -->
