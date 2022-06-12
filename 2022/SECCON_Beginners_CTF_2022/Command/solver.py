from pwn import *
from Crypto.Util.Padding import pad

def flip(d:bytes, offset:int, src:str, dst:str):
    src, dst = pad(src.encode(), 16), pad(dst.encode(), 16)
    assert len(src) == len(dst)
    d = bytearray(d)
    for i in range(len(src)):
        d[offset+i] = d[offset+i] ^ src[i] ^ dst[i]
    return bytes(d)

io = remote('command.quals.beginners.seccon.jp', 5555)

io.recvuntil('> ')
io.sendline('1')
io.recvuntil('> ')
io.sendline('fizzbuzz')
io.recvuntil('Encrypted command: ')

d = bytes.fromhex(io.recvline().strip().decode())
d = flip(d, 0, 'fizzbuzz', 'getflag')

io.recvuntil('> ')
io.sendline('2')
io.sendline(d.hex())

flag = io.recvline().decode()
print(flag)
