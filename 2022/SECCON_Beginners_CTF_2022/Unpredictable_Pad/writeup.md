# Writeup

以下のプログラムが与えられる。

```py
import random
import os


FLAG = os.getenv('FLAG', 'notflag{this_is_sample_flag}')


def main():
    r = random.Random()

    for i in range(3):
        try:
            inp = int(input('Input to oracle: '))
            if inp > 2**64:
                print('input is too big')
                return

            oracle = r.getrandbits(inp.bit_length()) ^ inp
            print(f'The oracle is: {oracle}')
        except ValueError:
            continue

    intflag = int(FLAG.encode().hex(), 16)
    encrypted_flag = intflag ^ r.getrandbits(intflag.bit_length())
    print(f'Encrypted flag: {encrypted_flag}')


if __name__ == '__main__':
    main()
```

`random.Random().getrandbits()` を予測することができればフラグが得られる。ただし、`getrandbits()`を実行して値が得られるのは3回までという制限がある。

`getrandbits()`は、Mersenne twisterで乱数を生成しており、32ビットの整数624個の出力を得られれば次の乱数が予測できる。

* [Mersenne Twisterの出力を推測してみる - ももいろテクノロジー](https://inaz2.hatenablog.com/entry/2016/03/07/194147)

この問題では、`if inp > 2**64:`という条件により、最大65ビット(2**64のとき)しか求められないように見えるが、負の値を入れることによって任意のビットの乱数を生成できる。

予測には`32 * 624 = 19968`ビット以上あればよいので、キリの良い8192ビットの乱数を3回生成してもらう。

あとは乱数予測すればXORで復号できる。

```py
from pwn import *
import re
from Crypto.Util.number import *
from mt19937predictor import MT19937Predictor

io = remote('unpredictable-pad.quals.beginners.seccon.jp', 9777)

v = -1 * (2 ** 8192 - 1) # 8192 bit integer
rands = []

for _ in range(3):
    io.recvuntil('Input to oracle: ')
    io.sendline(str(v))
    io.recvuntil("The oracle is: ")
    oracle = int(io.recvline().strip().decode())
    rands.append(oracle ^ v)

enc_flag = int(re.search(r'.*: ([0-9a-f]*)', io.recvline().decode()).group(1))

for i in range(230,280): # i found that enc_flag.bit_length() is in this range.
    pred = MT19937Predictor()
    for r in rands:
        pred.setrandbits(r, 8192)
    pr = pred.getrandbits(i)
    _flag = long_to_bytes(pr ^ enc_flag)
    if b'ctf4b' in _flag:
        print(_flag)
        break
```

<!-- ctf4b{M4y_MT19937_b3_w17h_y0u} -->
