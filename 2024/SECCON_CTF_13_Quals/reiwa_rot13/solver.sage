exec(open('reiwa_rot13/output.txt').read())

from Crypto.Util.number import *

# Analysis: See example of keys
import string
import random
import codecs
key = ''.join(random.sample(string.ascii_lowercase, 10))
rot13_key = codecs.encode(key, 'rot13')

key = key.encode()
rot13_key = rot13_key.encode()

print(f'{key=}, {bytes_to_long(key)=}')
print(f'{rot13_key=}, {bytes_to_long(rot13_key)=}')
print(f'{abs(bytes_to_long(key) - bytes_to_long(rot13_key))=:#022x}')

# From view point of each digits, appears only {0xf3, 0x0d, 0xf2, 0x0c}
# Looking from the last digit, 0xfx is followed by 0x0c or 0xf2.
# It is enough to do a full search to see if each digit is 0x0x or 0xfx.

# Compute all candidate of m1-m2
diff_candidate = [0 for _ in range(2**10)]
for i in range(2**10):
    diff = 0
    prev_digit = "0"
    for j in range(1,10+1):
        current_digit = f'{i:#012b}'[-j]
        if current_digit == "0":
            if prev_digit == "0":
                diff += (0x0d << (8*(j-1)))
            else:
                diff += (0x0c << (8*(j-1)))
        else:
            if prev_digit == "0":
                diff += (0xf3 << (8*(j-1)))
            else:
                diff += (0xf2 << (8*(j-1)))
        prev_digit = current_digit
    diff_candidate[i] = diff

assert abs(bytes_to_long(key) - bytes_to_long(rot13_key)) in diff_candidate

# Franklin-Reiter's Related Message Attack
PRx.<xn> = PolynomialRing(Zmod(n))

import tqdm
for k in tqdm.tqdm(diff_candidate):
    # https://furutsuki.hatenablog.com/entry/2020/06/07/192729#Crypto-Double-Message

    x = PRx.gen() # otherwise write xn
    g1 = x**e - c1
    g2 = (x + k)**e - c2

    # gcd
    while g2:
        g1, g2 = g2, g1 % g2

    g = g1.monic()
    if g.degree() != 1:
        continue

    # g = xn - msg
    msg = -g[0]
    key = long_to_bytes(msg)
    break

# AES Decrypt
import hashlib
from Crypto.Cipher import AES

hashed_key = hashlib.sha256(key).digest()
cipher = AES.new(hashed_key, AES.MODE_ECB)
decrypted_flag = cipher.decrypt(encyprted_flag)

print("Flag:", decrypted_flag.decode())
