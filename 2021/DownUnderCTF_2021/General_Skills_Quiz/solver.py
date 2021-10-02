from pwn import *
from urllib import parse
import base64
import codecs

io = remote('pwn-2021.duc.tf', 31905)

# Start
io.recvuntil('...')
io.sendline('')
# Q1
io.recvuntil(': ')
eq = io.recvline().decode().replace('=?','').strip()
ans = eval(eq)
io.sendline(str(ans))
# Q2
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = eval(eq)
io.sendline(str(ans))
# Q3
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = int(eq,16)
io.sendline(chr(ans))
# Q4
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = parse.unquote(eq)
io.sendline(ans)
# Q5
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = base64.b64decode(eq)
io.sendline(ans)
# Q6
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = base64.b64encode(eq.encode())
io.sendline(ans)
# Q7
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = codecs.decode(eq,'rot13')
io.sendline(ans)
# Q8
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = codecs.decode(eq,'rot13')
io.sendline(ans)
# Q9
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = eval(eq)
io.sendline(str(ans))
# Q10
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = bin(eval(eq))
io.sendline(str(ans))
# Q11
io.recvuntil('?')
io.sendline('DUCTF')

io.interactive()

io.close()
