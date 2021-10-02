import string

def encrypt(msg, f):
    return ''.join(chr(f.substitute(c)) for c in msg)

P.<x> = PolynomialRing(ZZ)
f = 13*x^2 + 3*x + 7

CHAR = string.printable
enc_dict = {}
for c in CHAR:
    enc_dict[str(encrypt(c.encode(), f))] = c

enc = open('output.txt', 'r').read().strip()
FLAG = ''
for e in enc:
    FLAG += enc_dict[e]
print(FLAG)
