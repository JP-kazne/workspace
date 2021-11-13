from pwn import *
from Crypto.Util.number import *

io = remote('aesnoc.crypto.wanictf.org', 50000)

cuts = lambda s : s.strip().replace('\'','')
sep = lambda c : [c[i:i+32] for i in range(0, len(c), 32)]
hex_xor = lambda a,b : hex(bytes_to_long(xor(bytes.fromhex(a.zfill(32)), bytes.fromhex(b.zfill(32)))))[2:]

io.recvuntil('iv = ')
iv = cuts(io.recvline().decode())
io.sendline('1')
io.recvuntil('encrypted_flag = ')
c = cuts(io.recvline().decode())

C = sep(c)

def encrypt(s):
    io.sendline('2')
    io.sendline(s)
    io.recvuntil('ciphertext = ')
    return cuts(io.recvline().decode())[:32]

p4 = '7d' + '0f' * 15
c = encrypt(p4)
p3 = hex_xor(hex_xor(c,iv),C[3])
c = encrypt(p3)
p2 = hex_xor(hex_xor(c,iv),C[2])
c = encrypt(p2)
p1 = hex_xor(hex_xor(c,iv),C[1])

flag = ''.join([bytes.fromhex(p).decode() for p in [p1,p2,p3,p4[:2]]])
print(flag)
