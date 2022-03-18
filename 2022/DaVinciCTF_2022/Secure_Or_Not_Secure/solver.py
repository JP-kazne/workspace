import base64
from pwn import *

io = remote('challs.dvc.tf', 2600)

# Register
io.recvuntil('>>> ')
io.sendline('2')
io.recvuntil(': ')
io.sendline('foo')
io.recvuntil(': ')
io.sendline('bar')
io.recvuntil(': ')
cookie = io.recvline()

io.recvuntil('>>> ')

d = base64.b64decode(cookie)

def flip(d:bytes, offset:int, src:str, dst:str):
    assert len(src) == len(dst)
    d = bytearray(d)
    for i in range(len(src)):
        d[offset+i] = d[offset+i] ^ ord(src[i]) ^ ord(dst[i])
    return bytes(d)

offset = len('username=foo\x00\x00\x00\x00\x00;admin=')
d = flip(d, offset, 'False', 'True;')
d = base64.b64encode(d)

# Login
io.sendline('1')
io.recvuntil(': ')
io.sendline(d)
print(io.recvuntil('>>> '))
