from pwn import *

io = remote('code.deadface.io', 50000)

msg = io.recvuntil('Your word is: ').decode()
print(msg)
word = io.recvline().decode().strip()
print(word)
s = sum([ord(w)-ord('a') for w in word])
io.sendline(str(s))

io.interactive()