# Writeup

与えられたファイルはgzipファイルなので展開する。

```bash
$ file Parcel 
Parcel: gzip compressed data, from Unix, original size modulo 2^32 759456

$ cp Parcel Parcel.gz

$ gzip -d Parcel.gz

$ file Parcel
Parcel_extract: multipart/mixed; boundary="===============6501672606206171874==", ASCII text, with very long lines
```

中身を見るとbase64エンコードされたpngファイルがいくつか見つかる。

```
--===============8130868917694707556==
Content-Type: image/png
MIME-Version: 1.0
Content-Transfer-Encoding: base64

iVBORw0KGgoAAAANSUhEUgAAA+gAAAGQAQAAAAAVNnfMAAAABGdBTUEAALGPC/xhBQAAACBjSFJN
AAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QAAd2KE6QAAAAHdElN
RQflBAkSOAgEM4oMAAAAxUlEQVR42u3NAQkAAAwDoPUvvcU4HC1geil2u91ut9vtdrvdbrfb7Xa7
3W632+12u91ut9vtdrvdbrfb7Xa73W632+12u91ut9vtdrvdbrfb7Xa73W632+12u91ut9vtdrvd
brfb7Xa73W632+12u91ut9vtdrvdbrfb7Xa73W632+12u91ut9vtdrvdbrfb7Xa73W632+12u91u
t9vtdrvdbrfb7Xa73W632+12u91ut9vtdrvdbrfb7Xa73W632+12++t9FESYDx8zamoAAAAldEVY
dGRhdGU6Y3JlYXRlADIwMjEtMDQtMDlUMTg6NTY6MDgrMDA6MDCnDaF3AAAAJXRFWHRkYXRlOm1v
ZGlmeQAyMDIxLTA0LTA5VDE4OjU2OjA4KzAwOjAw1lAZywAAAABJRU5ErkJggg==

--===============8130868917694707556==--
```

以下のプログラムで画像ファイルをすべて抽出する。

```py
import base64
import os
import re

with open(os.path.dirname(__file__)+'/Parcel_extract') as f:
    text = f.read()
    text = text.replace('\n','')
    b64s = re.findall(r'iVB.*?-',text)
    for index, b in enumerate(b64s):
        # print(index)
        img = base64.b64decode(b[0:-1])
        with open(f"{os.path.dirname(__file__)}/extract_img/image{index}.png", 'bw') as fi:
            fi.write(img)
```

断片的な画像ファイルが抽出できるのでつなぎ合わせる。

![](img/2021-04-11-21-56-05.png)

だいたいこんな感じ。

![](image_join.png)

<!-- RS{Im_doing_a_v1rtual_puzzl3} -->