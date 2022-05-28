n = 1216177716507739302616478655910148392804849
e = 65537
c1 = 257733734393970582988408159581244878149116
c2 = 843105902970788695411197846605744081831851

from factordb.factordb import FactorDB
from Crypto.Util.number import *

factor = FactorDB(n)
factor.connect()
factor = factor.get_factor_list()

p, q = factor
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
m1 = pow(c1, d, n)
m2 = pow(c2, d, n)
print(b''.join([long_to_bytes(m) for m in [m1,m2]]))
