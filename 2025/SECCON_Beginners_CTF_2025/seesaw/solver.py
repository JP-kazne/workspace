exec(open('seesaw/output.txt').read())

e = 65537
print(n, c)

from factordb.factordb import FactorDB
db = FactorDB(n)
db.connect()
factors = db.get_factor_list()
if len(factors) != 2:
    exit(1)

p, q = factors
phi = (p - 1) * (q - 1)
d = pow(e, -1 , phi)
m = pow(c, d, n)

from Crypto.Util.number import *
print(long_to_bytes(m))

# ctf4b{unb4l4nc3d_pr1m35_4r3_b4d}
