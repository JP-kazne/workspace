# Writeup

以下のプログラムが与えられる。

```py
print('Find my number N, and I will give you the flag.')
def f(N,k):
    while min(N,k)>0:
        if k>N: N,k = k,N
        N%=k
    return max(N,k)
import random
N = random.getrandbits(512)
for i in range(600):
    print(f"Try #{i+1}: ")
    k = input(f'Enter k: ')
    l = input(f'Enter l: ')
    try:
        k= int(k)
        assert 0<k<pow(10,500)
        l= int(l)
        assert 0<l<pow(10,500)
    except:
        print('Invalid input. Exiting...')
        quit()
    print(f'f(N+l,k) = {f(int(N+l),k)}\n')
guess = input('What is N?')
if str(N)==guess:
    print(open('flag.txt').read().strip())
else:
    print('Wrong answer. The number was '+str(N))
```

`f(N,k)`は`N`と`k`の最大公約数を求める関数である。

入力した`k,l`に対して、`f(N+l,k)`を計算してくれるので、この情報をもとに`N`を求める。

`N`は以下の例に示すアルゴリズムで、1ビットずつ求める。

```
例: N = 0b10011

1. GCD(N+2^0, 2^5)

    GCD(N+2^0, 2^5) = GCD(0b10100, 2^5) = 4

2. 4 >= 2^1

    Nに2^0を足して繰り上がることが分かるので、Nの0ビット目は **1**

3. GCD((N-1)+2^1, 2^5)

    GCD((N-1)+2^1, 2^5) = GCD(0b10100, 2^5) = 4

    0ビット目を0にして1ビット目を計算

4. 4 >= 2^2

    (N-1)に2^1を足して繰り上がることが分かるので、(N-1)の1ビット目は1 = Nの1ビット目は **1**

5. GCD((N-3)+2^2, 2^5)

    GCD((N-3)+2^2, 2^5) = GCD(0b10100, 2^5) = 4

    0,1ビット目を0にして2ビット目を計算

6. 4 < 2^3

    (N-3)に2^2を足しても繰り上がらないことが分かるので、(N-3)の2ビット目は0 = Nの2ビット目は **0**

以下繰り返し
```

以下のプログラムを実行してフラグが得られた。

```py
from pwn import *
from tqdm import tqdm

io = remote('ctf.k3rn3l4rmy.com', 2234)

N = 0
for i in tqdm(range(600)):
    io.recvuntil('Enter k: ')
    io.sendline(str(2**512))
    io.recvuntil('Enter l: ')
    io.sendline(str(-1*N + 2**i))
    io.recvuntil(' = ')
    gcd = int(io.recvline().strip())
    if gcd >= 2**(i+1):
        N += 2**i

io.recvuntil('What is N?')
io.sendline(N)
io.interactive()
```
<!-- flag{h4cking_th3_GCD!} -->
