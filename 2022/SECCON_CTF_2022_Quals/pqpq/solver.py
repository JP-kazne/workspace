from Crypto.Util.number import *

exec(open('output.txt').read())

a = (c1 + c2) % n
b = (c2 - c1) % n

p = GCD(a, n)
q = GCD(b, n)
r = n // (p * q)
assert n == p * q * r

phi = (p-1) * (q-1) * (r-1)
d = pow(e // 2, -1, phi)
m2 = pow(cm, d, n)

# Ref. https://github.com/sonickun/ctf-crypto-writeups/tree/master/2016/0ctf/rsa
# Ref. https://xornet.hatenablog.com/entry/2020/05/11/112508

# Tonelli–Shanks algorithm
from Crypto.Util.number import isPrime
def neg(x, n):
    return -x % n

def is_quadratic_residue(a, p):
    if a % p == 0:
        return True

    return legendre_symbol(a, p) == 1

def legendre_symbol(a, p):
    if not isPrime(p) or p == 2:
        raise ValueError("p must be a odd prime number")

    return pow(a, (p-1) // 2, p)

def get_q_s(p):
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    return (q, s)

def get_nonresidue(p):
    ret = 2
    while is_quadratic_residue(ret, p):
        ret += 1

    return ret

def tonelli_shanks(a, p):
    if not is_quadratic_residue(a, p):
        return ()

    if a == 0:
        return 0

    q, s = get_q_s(p)
    z = get_nonresidue(p)
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q+1) // 2, p)

    while True:
        if t == 1:
            return (r, neg(r, p))

        i = m
        for j in range(1, m):
            if pow(t, pow(2, j), p) == 1:
                i = j
                break

        b = pow(c, pow(2, m - i - 1), p)
        b_pow = pow(b, 2, p)
        m, c, t, r = i, b_pow, t * b_pow % p, r * b % p

# Chinese Remainder Theorem
from functools import reduce
def chinese_remainder(n, a):
	sum = 0
	prod = reduce(lambda a, b: a*b, n)
	for n_i, a_i in zip(n, a):
		p = prod // n_i
		sum += a_i * mul_inv(p, n_i) * p
	return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

_x, _y, _z = map(lambda mod:tonelli_shanks(m2, mod), [p, q, r])
from itertools import product
for x, y, z in product(_x, _y, _z): 
    m = long_to_bytes(chinese_remainder([p, q, r], [x, y, z]))
    if b'SECCON{' in m: 
        print(m)
        break

# SECCON{being_able_to_s0lve_this_1s_great!}
