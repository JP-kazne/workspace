# Writeup

ランダムな9byteをkeyにしてXORをとったPNGファイルが渡される。

PNGの先頭9byteは、file signature と IHDRチャンクの固定値が入るので、XORをとることによってkeyがわかる。

```py
import os
from pwn import xor

png_fixed9bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00'
e = open(os.path.dirname(__file__)+"/flag.png.enc","rb").read()
key = xor(e[0:9],png_fixed9bytes)
f = open(os.path.dirname(__file__)+"/flag.png","wb")
f.write(xor(e,key))
```

復号化した画像を見るとフラグが書かれている。

[参考]

* [PNG ファイルフォーマット](https://www.setsuki.com/hsp/ext/png.htm)

<!-- Hero{123_xor_321} -->