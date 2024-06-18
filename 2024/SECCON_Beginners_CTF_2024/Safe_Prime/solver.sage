from Crypto.Util.number import *

exec(open("Safe Prime/output.txt").read())
e = 65537

PR.<x> = PolynomialRing(ZZ)
f = x * (2*x + 1) - n
p = int(f.roots()[0][0])
q = n // p
assert p*q == n

d = power_mod(e, -1, (p-1)*(2*p))
m = power_mod(c, d, n)
print(long_to_bytes(m))
