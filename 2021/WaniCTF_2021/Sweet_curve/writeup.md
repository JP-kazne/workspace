# Writeup

以下のテキストが与えられる。

```
# Given:
# - An elliptic curve: y**2 = x**3 - x + 1 (mod p)
# - Two points: P(x_P, y_P) and Q(x_Q, y_Q)

# Find the point P+Q
# The flag is the x value of P+Q
# Don't forget to convert it into a string!
p = 0x89a4e2c7f834f5fbc6f2a314e373e3723de7df6283c5d97cbca509c61e02965b7ef96efce1d827bfdfa7f21d22803558bb549f9ea15dfe9f47d3976648c55feb
x_P = 0x1e1cba0e07c61cf88e9f23b9859093c33c26cf83bcfb6fe24d7559cd0ea86fb2f144ae643ac5edf6f04ef065dc7c2c18d88ae02843592d5e611029fefc0fece
y_P = 0x198420b30a4330f82380326895d0ac06a1859bc49d45cd4b08021b857d23d515163b9151fbaf7ae5f816d485d129d3b1c4630d1fb45c6790af551428a5c85667
x_Q = 0x7e32edfd7befd8df93d7b738d6a1c95e1cfd56b3a6ccc4a62e4e0ae9059b4903e71fccbe07d8d45c762b4a3ed5c9d1a2505043d033e58adb72191259b81bc47d
y_Q = 0x46016c676585feaf048fff9d5cbb45dbd598c6c4c81694e0881bf110b57012f0bac6eaf7376fee015c8cecba1fc92206ca346f7d72ee1d60f820091c85fa76b3
```

`y**2 = x**3 - x + 1 (mod p)`のとき、以下の計算式で、`R = P + Q`の点を計算することができる。

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/e144863e44d7963bc5d411b7a305d591b893ae82)

* https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_addition

```py
from Crypto.Util.number import *

exec(open('cry-sweet-curve/parameters.txt').read())

_lambda = (((y_Q - y_P) % p) * pow((x_Q - x_P), -1, p)) % p
x_R = (pow(_lambda, 2, p) - x_P - x_Q ) % p
print(long_to_bytes(x_R))
```

<!-- FLAG{7h1s_curv3_alw@ys_r3m1nd5_me_0f_pucca} -->