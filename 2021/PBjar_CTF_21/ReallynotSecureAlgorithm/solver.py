from Crypto.Util.number import *

f = open('ReallynotSecureAlgorithm/out.txt', 'r').read().splitlines()
[p, q, e, ct] = list(map(int, f))

d = pow(e, -1, (p-1)*(q-1))
m = pow(ct, d, p*q)
print(long_to_bytes(m))
