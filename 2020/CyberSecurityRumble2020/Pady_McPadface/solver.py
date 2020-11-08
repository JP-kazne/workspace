# Original https://ctftime.org/writeup/24770

from pwn import *
from Crypto.Util.number import long_to_bytes

context.log_level = "error"

# get jacobi symbol
def jacobi(a, n):
    assert(n > a > 0 and n%2 == 1)
    t = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0

n=23946008544227658126007712372803958643232141489757386834260550742271224503035086875887914418064683964046938371640632153677880813529023769841157840969433316734058706481517878257755290676559343682013294580085557476138201639446709290119631383493940405818550255561589074538261117055296294434994144540224412018398452371792093095280080422459773487177339595746894989682038387107119249733105558301840478252766907821053044992141741079156669562032221433390029219634673005161989684970682781410366155504440886376453225497112165607897302209008685179791558898003720802478389914297472563728836647547791799771532020349546729665006643

HOST = 'chal.cybersecurityrumble.de'
PORT = 34187
L = 263 # number of bits to retrieve

sols = [0 for _ in range(L)]
for i in range(100):
    r = remote(HOST,PORT)
    res = r.recvall().split(b"\n")
    cs = []
    for l in res:
        try:
            cs.append(int(l))
        except:
            pass
    assert len(cs) == L
    for j,c in enumerate(cs):
        if jacobi(c,n) == -1: # we are sure that it's not a square
            sols[j] = 1
    print( long_to_bytes( int("".join(map(str,sols)),2)).decode("utf-8") )