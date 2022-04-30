from pwn import *
from Crypto.Util.number import *
from tqdm import tqdm

io = remote('ctf.b01lers.com', 9003)
io.recvuntil('Select a difficulty (1/2):')
io.sendline('1')
msg = io.recvuntil('\n\n')

plain_bin = ''

for i in tqdm(range(256)):
    check_bin = '0'*i + '1' + '0'*(255-i)

    io.sendline(check_bin)
    msg = io.recvline()
    if b'1' in msg:
        plain_bin += '1'
    else:
        plain_bin += '0'

print(long_to_bytes(int(plain_bin, 2)))
