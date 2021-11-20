from pwn import *
from tqdm import tqdm

io = remote('ctf.k3rn3l4rmy.com', 2234)

N = 0
for i in tqdm(range(600)):
    io.recvuntil('Enter k: ')
    io.sendline(str(2**512))
    io.recvuntil('Enter l: ')
    io.sendline(str(-1*N + 2**i))
    io.recvuntil(' = ')
    gcd = int(io.recvline().strip())
    if gcd >= 2**(i+1):
        N += 2**i

io.recvuntil('What is N?')
io.sendline(N)
io.interactive()
