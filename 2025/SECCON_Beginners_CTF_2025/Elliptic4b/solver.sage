from fastecdsa.curve import secp256k1
from fastecdsa.point import Point

from pwn import *

io = remote('elliptic4b.challenges.beginners.seccon.jp','9999')
io.recvuntil("y = ")
y = int(io.recvline().decode())
print(y)


# https://pebble8888.hatenablog.com/entry/2017/10/18/010303
p = secp256k1.p
F = GF(p)
E = EllipticCurve(F, [0, 7]) # secp256k1: y^2 = x^3 + 7
y = F(y)

rhs = y^2 - 7
cubic_x = rhs.nth_root(3, all=True)
group_order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

if len(cubic_x) == 0:
    exit(1)


for _x in cubic_x:
    if secp256k1.is_point_on_curve((_x, y)):
        x = _x
        P = Point(x, y, secp256k1)
        Q = int(group_order - 1) * P
        if P.x != Q.x:
            print("// x-coordinates do not match!")
            continue
        if P.y == Q.y:
            print("// P and Q are the same point!")
            continue
        break

io.sendlineafter("x = ", str(int(x)))
io.sendlineafter("a = ", str(group_order - 1))
print(io.recvall())

# ctf4b{1et'5_b3c0m3_3xp3r7s_1n_3ll1p71c_curv35!}
