from Crypto.Util.number import *
import itertools
import math

exec(open("dist/output.txt").read())

# n = p*q
# phi = p*q - (p+q) + 1
# e*d = 1 + k*phi

# Factorize (e*d - 1) by using FactorDB
k_factors = [2,2,2,2,5,7,23,43,67,1181,7591,7658627]
# 2^12 at most, so brute force
for n in range(len(k_factors)):
    for conb in itertools.combinations(k_factors, n+1):
        k = math.prod(list(conb))
        phi = (e*d - 1)//k
        assert e*d - 1 == k* phi
        n = phi + hint - 1
        if b'SECCON{' in long_to_bytes(pow(c,d,n)):
            print(long_to_bytes(pow(c,d,n)))
            exit()

# SECCON{thank_you_for_finding_my_n!!!_GOOD_LUCK_IN_SECCON_CTF}
