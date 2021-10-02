from factordb.factordb import FactorDB
from Crypto.Util.number import *

f = open('Not_Baby/out.txt', 'r').read().replace(':','=')
n, e, ct = 0, 0, 0
exec(f)

factor = FactorDB(n)
factor.connect()
factor = factor.get_factor_list()

phi = 1
for fc in factor:
    phi *= (fc-1)
d = pow(e,-1,phi)
m = pow(ct,d,n)
print(long_to_bytes(m))
