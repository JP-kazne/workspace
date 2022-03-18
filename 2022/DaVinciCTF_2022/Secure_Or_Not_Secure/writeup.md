# Writeup

```
$ nc challs.dvc.tf 2600
------ Welcome to my secure login system ------
1. Login
2. Register
3. Exit
-----------------------------------------------
>>> 1
Cookie: a
Are you trying to cheat?!
------ Welcome to my secure login system ------
1. Login
2. Register
3. Exit
-----------------------------------------------
>>> 2
Username: foo
Password: bar
Here is your cookie: N1xXIW4JbpNKXeNxmaB0llzlOVJMmhdXUMtvuA2n44ZeU+rUhWIdS8I9brn38x4qdGoRs7eQsw==
------ Welcome to my secure login system ------
1. Login
2. Register
3. Exit
-----------------------------------------------
>>> 1
Cookie: N1xXIW4JbpNKXeNxmaB0llzlOVJMmhdXUMtvuA2n44ZeU+rUhWIdS8I9brn38x4qdGoRs7eQsw==
You're not the admin! The cookie b'username=foo\x00\x00\x00\x00\x00;admin=False;password=bar\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' is invalid!
```

ブロックごとにパラメータが割り振られていて、`admin=True;`にできれば良さそうなので、Bit Flipping Attackで改ざんを試みたところ、うまくいった。

```py
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
```

<!-- dvCTF{42d71e9ee0f5205b54213b10d39c548f} -->
