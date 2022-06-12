# Writeup

以下のプログラムが与えられる。

```py
from Crypto.Util.number import *
from secret import flag
from functools import reduce
from operator import mul


bits = 256
flag = bytes_to_long(flag.encode())
assert flag.bit_length() == 455

GUESTS = []


def invite(p):
    global GUESTS
    if isPrime(p):
        print("[*] We have been waiting for you!!! This way, please.")
        GUESTS.append(p)
    else:
        print("[*] I'm sorry... If you are not a Prime Number, you will not be allowed to join the party.")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-")


invite(getPrime(bits))
invite(getPrime(bits))
invite(getPrime(bits))
invite(getPrime(bits))

for i in range(3):
    print("[*] Do you want to invite more guests?")
    num = int(input(" > "))
    invite(num)


n = reduce(mul, GUESTS)
e = 65537
cipher = pow(flag, e, n)

print("n =", n)
print("e =", e)
print("cipher =", cipher)
```

256ビットの素数4つと、ユーザーが与える最大3つの素数でRSA暗号の暗号化を行っている。

自分で素数を与えられるので、`flag.bit_length() == 455`よりも大きな素数`p`を与えることによって

$$cipher = m^e \mod n$$

ではなく、

$$cipher = m^e \mod p$$

で計算できるようになる。

```py
from pwn import *
from Crypto.Util.number import *


io = remote('primeparty.quals.beginners.seccon.jp', 1336)

primes = [getPrime(500) , 1, 1]

for p in primes:
    io.recvuntil('> ')
    io.sendline(str(p))

io.recvuntil('n = ')
n = int(io.recvline().decode().strip())
io.recvuntil('e = ')
e = int(io.recvline().decode().strip())
io.recvuntil('cipher = ')
c = int(io.recvline().decode().strip())

p = primes[0]
qr = n // p

d = pow(e,-1,(p-1))
m = pow(c,d,p)

print(long_to_bytes(m))
```


<!-- ctf4b{HopefullyWeCanFindSomeCommonGroundWithEachOther!!!} -->
