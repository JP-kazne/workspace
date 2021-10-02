from string import ascii_lowercase, digits
CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits
n = len(CHARSET)

def encrypt(msg, f):
    ct = ''
    for c in msg:
        ct += CHARSET[f.substitute(CHARSET.index(c))]
    return ct

P.<x> = PolynomialRing(GF(n))
enc = open('output.txt', 'r').read().strip()
# f = P.random_element(6)
# f = a0*x^6 + a1*x^5 + a2*x^4 + a3*x^3 + a4*x^2 + a5*x + a6

mat = []
for i in range(7):
    mat.append([i^6, i^5, i^4, i^3, i^2, i^1, i^0])    
M = Matrix(P, mat)
vec = [CHARSET.index(enc[i]) for i in range(6)]
vec.append(CHARSET.index(enc[-1]))
b = vector(P, vec)
solve = M.solve_right(b)

f = solve[0]*x^6 + solve[1]*x^5 + solve[2]*x^4 + solve[3]*x^3 + solve[4]*x^2 + solve[5]*x + solve[6]

enc_dict = {}
for c in CHARSET:
    enc_dict[c] = encrypt(c, f)

FLAG = ''
for e in enc:
    tmp = ''
    for key, value in enc_dict.items():
        if value == e:
            tmp += key
    if len(tmp) == 1:
        FLAG += tmp
    else:
        FLAG += '[' + tmp + ']'
print(FLAG)
