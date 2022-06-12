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
