# Writeup

以下のテキストファイルが与えられる。

```
666c61677b6469735f69735f615f666c346767675f68317d
```

ASCIIコードを変換するとフラグが得られた。

```
$ python3
>>> from Crypto.Util.number import *
>>> long_to_bytes(0x666c61677b6469735f69735f615f666c346767675f68317d)
b'flag{dis_is_a_fl4ggg_h1}'
```

<!-- flag{dis_is_a_fl4ggg_h1} -->
