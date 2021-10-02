# Writeup

`flag.txt`というバイナリファイルが与えられる。ファイル識別子を見ると、圧縮されたファイル形式であることが分かるので、何度も解凍していく。

```py
import bz2
import zipfile
import lzma
import gzip
import os

with open('flag', 'wb') as tmp:
    f = open('flag.txt', 'rb').read()
    tmp.write(f)

while True:
    sign = b''
    with open('flag', 'rb') as tmp:
        sign = tmp.read()[:4]

    if sign == b'BZh9':
        with bz2.open('flag', 'rb') as f, open('tmp', 'wb') as tmp:
            tmp.write(f.read())
        os.system('rm flag')
        os.system('mv tmp flag')
    elif sign == b'PK\x03\x04':
        with zipfile.ZipFile('flag') as f:
            f.extractall('./tmp')
        os.system('rm flag')
        os.system('mv tmp/flag.txt flag')
        os.system('rm -rf tmp')
    elif sign == b'\xfd7zX':
        with lzma.open('flag', 'rb') as f, open('tmp', 'wb') as tmp:
            tmp.write(f.read())
        os.system('rm flag')
        os.system('mv tmp flag')
    elif sign == b'\x1f\x8b\x08\x08':
        with gzip.open('flag', mode='rb') as f, open('tmp', 'wb') as tmp:
            tmp.write(f.read())
        os.system('rm flag')
        os.system('mv tmp flag')
    else:
        print(sign)
        break
```

上記のスクリプトを実行すると、以下のテキストファイルが得られた。

```
RFVDVEZ7YmFidXNoa2FzX3YwZGthX3dhc19oM3IzfQ==
```

Base64デコードしたところ、フラグが得られた。

<!-- DUCTF{babushkas_v0dka_was_h3r3} -->
