# Writeup

ユーザー名の入力フォームがあり、内部では

```
{"admin": false, "username": username}
```

をCBCモードで暗号化した値を、Cookieにセットしている。

`username`を`admin`としてログインしたところ、以下の値がCookieにセットされた。

```
yH8E9m039e1rav+2S/kIX2D8eEJk/Gf5VvsBv7LI//6WwmnffTTHMJqPuZmw7sNbPO9VnxWbP3CK8NcWgmYSwg==
```

Bit Flipping Attackで先頭ブロックを書き換え、復号したときに"admin"のkeyがtrueになるような値をCookieにセットする。

```
{"admin": false, "username": "admin"}

⇒

{"admin":  true, "username": "admin"}
```

```py
import base64

d = 'yH8E9m039e1rav+2S/kIX2D8eEJk/Gf5VvsBv7LI//6WwmnffTTHMJqPuZmw7sNbPO9VnxWbP3CK8NcWgmYSwg=='
d = base64.b64decode(d)

def flip(d:bytes, offset:int, src:str, dst:str):
    assert len(src) == len(dst)
    d = bytearray(d)
    for i in range(len(src)):
        d[offset+i] = d[offset+i] ^ ord(src[i]) ^ ord(dst[i])
    return bytes(d)

offset = len('{"admin": ')
d = flip(d, offset, 'false', ' true')
d = base64.b64encode(d)
print(d)
```

Cookieに`yH8E9m039e1rarmjVf8IX2D8eEJk/Gf5VvsBv7LI//6WwmnffTTHMJqPuZmw7sNbPO9VnxWbP3CK8NcWgmYSwg==`をセットして再読み込みするとフラグが得られた。

![](img/2021-11-06-23-25-41.png)

<!-- FLAG{Fl1p_Flip_Fl1p_Flip_Fl1p____voila!!} -->
