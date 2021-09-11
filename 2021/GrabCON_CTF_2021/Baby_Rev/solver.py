from Crypto.Util.number import *

C = [0x99dfdf8d, 0x9de2f094, 0x7830acdf8d8b, 0x5feadadf96, 0x5f33b8cb8fdf]

flag = b''
for c in C:
    flag += long_to_bytes(c^0xdeadbeef)
print(flag + b'}')
