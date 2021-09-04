lines = open('discrete-log/output.txt').read().splitlines()
p, g = int(lines[0]), int(lines[1])
cs = list(map(int,lines[2][1:-1].split(',')))

# make g^r from known words
# CakeCTF{} = [67, 97, 107, 101, 67, 84, 70, 123, ... , 125]
cs7_inv = pow(cs[7],-1,p)
g2r = (cs[-1]*cs7_inv) % p
cs4_inv = pow(cs[4],-1,p)
g17r = (cs[5]*cs4_inv) % p
g1r = (pow(g2r,9,p) * pow(g17r,-1,p)) % p
g1r_inv = pow(g1r,-1,p)

table = {}
exp = 0
i = 67
while i < 0x7f:
    table[(cs[0]*(g1r**exp))%p] = chr(i)
    exp += 1
    i += 1

exp = 0
i = 67
while i > 0x20:
    table[(cs[0]*(g1r_inv**exp))%p] = chr(i)
    exp += 1
    i -= 1

flag = ''
for c in cs:
    if c in table.keys():
        flag += table[c]
    else:
        flag += '?'

print(flag)
