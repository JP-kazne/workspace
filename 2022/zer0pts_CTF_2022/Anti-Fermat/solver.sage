# sage
from Crypto.Util.number import *

if __name__ == '__main__':
    exec(open('anti_fermat/output.txt').read())
    _p = var('_p')
    s = solve([_p*_p + n == _p*((1<<1024)-1)],_p)
    p = Integer(s[1].rhs().n(1024))
    while True:
        q = n // p
        if p*q == n:
            break
        p += 1

    phi = int((p-1)*(q-1))
    d = power_mod(65537, -1, phi)
    m = power_mod(c,d,n)
    print(long_to_bytes(m))

