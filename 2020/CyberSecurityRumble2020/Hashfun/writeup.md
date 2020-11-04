# Writeup

以下のPythonプログラムが与えられる。

```py
from secret import FLAG

def hashfun(msg):
    digest = []
    for i in range(len(msg) - 4):
        digest.append(ord(msg[i]) ^ ord(msg[i + 4]))
    return digest

print(hashfun(FLAG))
# [10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]
```

コメント行部分が出力であると推測できる。

`hashfun()`の動作は以下の通り。

* `ord()`でASCIIコード(10進)に変換

`CSR{flag}` ⇒ `67 83 82 123 102 108 97 103 125`

* 4つ先の文字とXORを計算

`67(C) ^ 102(f) = 37`,  
`83(S) ^ 108(l) = 63`,  
`82(R) ^ 97(a) = 51`,  
`123({) ^ 103(g) = 28`,  
`102(f) ^ 125(}) = 27`  

`hashfun('CSR{flag}') = [37, 63, 51, 28, 27]`

つまり、`67(c) ^ ???(?) = 10` の `???`を求められればよい。

XORは2回作用させると元に戻る性質があるので、`10 ^ 67 = ??? = 73(I)` となる。

* [競技プログラミングにおけるXORのTips](https://qiita.com/kuuso1/items/778acaa7011d98a3ff3a)

`FLAG`を求めるプログラムを作成

```py
digest = [10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]
char = 'CSR{'

i = 0
for d in digest:
    x = chr(d ^ ord(char[i]))
    char += x
    i += 1

print(char)
```

<!-- CSR{IMMERDIESEMATHEMATIK} -->
