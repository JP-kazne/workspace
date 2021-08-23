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