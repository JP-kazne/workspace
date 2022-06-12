# Writeup

以下のプログラムが与えられる。

```py
from random import shuffle

flag = b"ctf4b{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"

cipher = []

for i in range(len(flag)):
    f = flag[i]
    c = (f + i)**2 + i
    cipher.append(c)

shuffle(cipher)
print("cipher =", cipher)
```

`c = (f + i)**2 + i` でフラグが暗号化されているので、逆操作で復号する。

スクリプトは以下。

```py
cipher = []
exec(open('output.txt').read())

# (f+i)**2 が取りうる値をリスト化
square_numbers = [(i, i**2) for i in range(0x20, 0x7F + len(cipher))]

flag_dec = [0 for _ in range(len(cipher))]
for c in cipher:
    diff = [abs(c-n2) for _, n2 in square_numbers]
    # i の値を特定
    idx = min(diff)
    # (f+i)**2 をリストにいれる
    flag_dec[idx] = square_numbers[diff.index(idx)]

flag = ''
for idx, f in enumerate(flag_dec):
    n, _ = f
    # (f+i)-i を求める
    flag += chr(n-idx)

print(flag)
```

<!-- ctf4b{Hey,Fox?YouCanNotTearThatHouseDown,CanYou?} -->
