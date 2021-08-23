from pwn import *
from Crypto.Util.number import *

out = open('task/output.txt', 'r').read().splitlines()
[p, q, r] = list(map(int,out[0].split(' ')))
c = binascii.unhexlify(out[1][2:-1])

flag = xor(c, long_to_bytes(2*q))
print(flag)