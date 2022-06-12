from pwn import *
import re
from Crypto.Util.number import *
from mt19937predictor import MT19937Predictor

io = remote('unpredictable-pad.quals.beginners.seccon.jp', 9777)

v = -1 * (2 ** 8192 - 1) # 8192 bit integer
rands = []

for _ in range(3):
    io.recvuntil('Input to oracle: ')
    io.sendline(str(v))
    io.recvuntil("The oracle is: ")
    oracle = int(io.recvline().strip().decode())
    rands.append(oracle ^ v)

enc_flag = int(re.search(r'.*: ([0-9a-f]*)', io.recvline().decode()).group(1))

for i in range(230,280): # i found that enc_flag.bit_length() is in this range.
    pred = MT19937Predictor()
    for r in rands:
        pred.setrandbits(r, 8192)
    pr = pred.getrandbits(i)
    _flag = long_to_bytes(pr ^ enc_flag)
    if b'ctf4b' in _flag:
        print(_flag)
        break

