from Crypto.Util.number import *

n, e, c = 0, 0, 0
exec(open('pppp/output.txt').read())

p = GCD(n, c[0][0]) # c[0][0] = (p*r)^e
q = n // p
assert p*q == n
d = int(pow(e, -1, (p-1)*(q-1)))

m = matrix(Zmod(n), c)^d

flag = long_to_bytes(GCD(int(m[1][1]),int(m[1][2])))
flag += long_to_bytes(GCD(int(m[2][2]),int(m[2][3])))

print(flag)
