from Crypto.Util.number import *
import itertools
import math

exec(open("math/output.txt").read())

af = 4701715889239073150754995341656203385876367121921416809690629011826585737797672332435916637751589158510308840818034029338373257253382781336806660731169
bf = 35760393478073168120554460439408418517938869000491575971977265241403459560088076621005967604705616322055977691364792995889012788657592539661
_ab = ab // ((af**2) * (bf**2))
# _ab = (3 · 173 · 199 · 306606827773<12>)^2
# print(_ab)

PR.<X> = PolynomialRing(ZZ)

factors = [3, 173, 199, 306606827773, af, bf]
for i in range(len(factors)):
    for c in itertools.combinations(factors, i):
        a = math.prod(c) ** 2
        b = ab // a
        f = (X + a)*(X + b) - n
        if f.roots() == []:
            continue
        x = int(f.roots()[0][0])
        p = a + x
        q = b + x
        d = power_mod(e, -1, (p-1)*(q-1))
        m = power_mod(cipher, d, n)
        print(long_to_bytes(m))
