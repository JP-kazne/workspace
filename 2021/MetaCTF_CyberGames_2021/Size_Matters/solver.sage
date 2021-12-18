from Crypto.Util.number import *

c = 0x2526512a4abf23fca755defc497b9ab
e = 257
n = 0x592f144c0aeac50bdf57cf6a6a6e135

f = [f[0] for f in list(factor(n)) for _ in range(f[1])]
assert len(f) == 2
p, q = f
d = pow(e, -1, (p-1)*(q-1))
m = pow(c, d, n)
print(long_to_bytes(m))
