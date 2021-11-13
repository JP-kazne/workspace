from pwn import *

with open('cry-dango/output.txt') as f:
    ciphertext = bytes.fromhex(f.readline().split(' : ')[1].strip())
    A = bytes.fromhex(f.readline().split(' : ')[1].strip())
    B = bytes.fromhex(f.readline().split(' : ')[1].strip())
    C = bytes.fromhex(f.readline().split(' : ')[1].strip())

key0 = xor(A,C)
flag = xor(ciphertext,key0)
print(flag)
