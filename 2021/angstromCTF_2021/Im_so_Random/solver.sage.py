

# This file was *autogenerated* from the file solver.sage
from sage.all_cmdline import *   # import sage library

_sage_const_8 = Integer(8); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_6 = Integer(6); _sage_const_99999999 = Integer(99999999); _sage_const_10000000 = Integer(10000000)
import os
os.environ['PWNLIB_NOTERM'] = 'True' # sage & pwntools

from pwn import *
import re
import itertools

class Generator():
    DIGITS = _sage_const_8 
    def __init__(self, seed):
        self.seed = seed
        assert(len(str(self.seed)) == self.DIGITS)

    def getNum(self):
        self.seed = int(str(self.seed**_sage_const_2 ).rjust(self.DIGITS*_sage_const_2 , "0")[self.DIGITS//_sage_const_2 :self.DIGITS + self.DIGITS//_sage_const_2 ])
        return self.seed

io = remote('crypto.2021.chall.actf.co','21600')

io.sendline('r')
r1 = int(re.search(r'\d+', io.recvline().decode('utf-8')).group())
print(r1)
io.sendline('r')
r2 = int(re.search(r'\d+', io.recvline().decode('utf-8')).group())
print(r2)
F = factor(r1)
f = [f[_sage_const_0 ] for f in F for _ in range(f[_sage_const_1 ])]
if len(f) >= _sage_const_6 :
    io.close()
    exit()
perm = [p for p in itertools.permutations(f)]
found = False
for p in perm :
    a = _sage_const_1 
    for n in p:
        if a * n < _sage_const_99999999 :
            a *= n
        else:
            break
    b = r1 // a
    if _sage_const_10000000  <= a <= _sage_const_99999999  and  _sage_const_10000000  <= b <= _sage_const_99999999 :
        g1 = Generator(a)
        g2 = Generator(b)
    else:
        continue
    if(g1.getNum()*g2.getNum() == r2):
        found = True
        break
if found:
    io.sendline('g')
    io.sendline(str(g1.getNum()*g2.getNum()))
    io.sendline(str(g1.getNum()*g2.getNum()))
    io.interactive()

