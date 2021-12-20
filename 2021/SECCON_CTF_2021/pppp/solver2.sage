from Crypto.Util.number import *

n, e, c = 0, 0, 0
exec(open('pppp/output.txt').read())

p = GCD(n, c[0][0]) # c[0][0] = (p*r)^e
q = n // p
assert p*q == n
d = int(pow(e, -1, (p-1)*(q-1)))

m1s = pow(c[1][1], d, n) # c[1][1] = (m1*s)^e
m2t = pow(c[2][2], d, n) # c[2][2] = (m2*t)^e
# print(m1s)
# print(m2t)

flag = b''
### factorize m1s in Msieve ###
# p1: 2
# p2: 11
# p2: 11
# p3: 101
# prp11: 17733194681
# prp11: 21989360161
# prp21: 194838390862027996463
# prp231: 890941089701337639742923670629764992383197102649368033477055542426171609788212371754143394788213291456300216361551640449365841636339404366563906765128981689755176699342918904671528454362377482743831820969956624190146702130809843851
flag += long_to_bytes(2*11*11*101*17733194681*21989360161*194838390862027996463)

### m2t can't factorize in Msieve ###
### So, find another solution ###
u = pow(c[3][3], d, n) # c[3][3] = u^e

expr = 0
for i in range(e):
    expr += (pow(u,i,n) * pow(m2t,(e-1)-i,n))%n
    expr %= n

m2v = (pow(expr, -1, n) * c[2][3]) % n # m2*t*expr = c[2][3]
flag += long_to_bytes(GCD(int(m2t),int(m2v)))

print(flag)

