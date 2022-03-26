# Writeup

以下のプログラムとその出力が与えられる。

```py
from Crypto.Util.number import isPrime, getStrongPrime
from gmpy import next_prime
from secret import flag

# Anti-Fermat Key Generation
p = getStrongPrime(1024)
q = next_prime(p ^ ((1<<1024)-1))
n = p * q
e = 65537

# Encryption
m = int.from_bytes(flag, 'big')
assert m < n
c = pow(m, e, n)

print('n = {}'.format(hex(n)))
print('c = {}'.format(hex(c)))
```

RSA暗号で、素数 ![p](https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bblack%7D%5Cdisplaystyle+p) に対し ![q](https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bblack%7D%5Cdisplaystyle+q) を

![q = p \oplus (2^1024 -1) + \alpha](https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bblack%7D%5Cdisplaystyle+q+%3D+p+%5Coplus+%282%5E1024+-1%29+%2B+%5Calpha)

で計算している。ここで、

![p \oplus (2^1024 -1) = \overline p](https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bblack%7D%5Cdisplaystyle+p+%5Coplus+%282%5E1024+-1%29+%3D+%5Coverline+p)

である。

すると、以下2つの等式が成り立つので、![p](https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bblack%7D%5Cdisplaystyle+p) について連立方程式を解けばよい。 (1)式は近似なので、周辺の整数解を探索する。

![\begin{align}
n \simeq p \overline p \\
p + \overline p = 2^1024 - 1
\end{align}](https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bblack%7D%5Cdisplaystyle+%5Cbegin%7Balign%7D%0An+%5Csimeq+p+%5Coverline+p+%5C%5C%0Ap+%2B+%5Coverline+p+%3D+2%5E1024+-+1%0A%5Cend%7Balign%7D)

```py
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
```

整数解 ![p](https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bblack%7D%5Cdisplaystyle+p) からRSA暗号を復号すればフラグが得られる。

<!-- zer0pts{F3rm4t,y0ur_m3th0d_n0_l0ng3r_w0rks.y0u_4r3_f1r3d} -->
