from pwn import *
from Crypto.Util.number import *

n,e,c,s = 0,0,0,0

conn = remote('choice.beginners.seccon.games', 1336)
exec(conn.recvline_startswith('n ='))
exec(conn.recvline_startswith('e ='))
exec(conn.recvline_startswith('c ='))
exec(conn.recvline_startswith('s ='))

# phi = (p-1)(q-1)(r-1) = n - s + p + q + r - 1

# find X = p + q + r
## a_{n+2} = X * a_{n+1} - s * a_{n} mod n
## <=>
## X = ( a_{n+2} + s * a_{n} ) * ( a_{n+1} ) ^ -1
conn.sendline(str(n+2))
conn.recvuntil('result_a : ')
X_N2 = int(conn.recvline().decode())
conn.sendline(str(n+1))
conn.recvuntil('result_a : ')
X_N1 = int(conn.recvline().decode())
conn.sendline(str(n))
conn.recvuntil('result_a : ')
X_N0 = int(conn.recvline().decode())
X = ((X_N2 + s * X_N0) * pow(X_N1, -1, n)) % n

phi = n - s + X - 1
d = pow(e, -1, phi)
m = long_to_bytes(pow(c, d, n))

print(m)

# <!-- ctf4b{E4sy_s7mmetr1c_polyn0mial} -->
