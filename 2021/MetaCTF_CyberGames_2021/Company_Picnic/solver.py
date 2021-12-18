from Crypto.Util.number import *
import gmpy2

f = open('public_keys.txt').readlines()
f = [l.strip() for l in f] # remove \n
while '' in f:
    f.remove('')

def rational_to_quotients(x, y):
    a = x // y
    quotients = [a]
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        quotients.append(a)
    return quotients

def convergents_from_quotients(quotients):
    convergents = [(quotients[0], 1)]
    for i in range(2, len(quotients) + 1):
        quotients_partion = quotients[0:i]
        denom = quotients_partion[-1]
        num = 1
        for _ in range(-2, -len(quotients_partion), -1):
            num, denom = denom, quotients_partion[_] * denom + num
        num += denom * quotients_partion[0]
        convergents.append((num, denom))
    return convergents

def WienerAttack(e, n):
    quotients = rational_to_quotients(e, n)
    convergents = convergents_from_quotients(quotients)
    for (k, d) in convergents:
        if k and not (e * d - 1) % k:
            phi = (e * d - 1) // k
            # check if (x^2 - coef * x + n = 0) has integer roots
            coef = n - phi + 1
            delta = coef * coef - 4 * n
            if delta > 0 and gmpy2.iroot(delta, 2)[1] == True:
                return d

idx = 0
N, e = 0, 0
flag = b''
while idx < len(f):
    exec(f[idx]) # N
    idx += 1
    exec(f[idx]) # e
    idx += 1

    d = WienerAttack(e, N)
    if d is not None:
        flag += long_to_bytes(d)
print(flag)
