from Crypto.Util.number import *
from random import getrandbits

key, cipher = 0, 0
exec(open('Conquer/output.txt').read())

# Rotation Right
def ROR(bits, N):
    for _ in range(N):
        bits = (bits >> 1) | ((bits & 0x1) << (length - 1))
    return bits

length = key.bit_length() + 1
for i in range(32):
    cipher ^= key
    key = ROR(key, pow(cipher, 3, length))

print(long_to_bytes(cipher^key))

# <!-- ctf4b{SemiCIRCLErCanalsHaveBeenConqueredByTheCIRCLE!!!} -->
