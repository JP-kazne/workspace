from Crypto.Util.number import *

exec(open('output.txt').read())

d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
