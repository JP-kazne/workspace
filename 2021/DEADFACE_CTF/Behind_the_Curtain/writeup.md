# Writeup

画像ファイルが与えられる。

binwalkコマンドを実行したところ、さらに画像ファイルがあることが分かった。

```bash
$ binwalk -e steg01.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
13266         0x33D2          JPEG image data, JFIF standard 1.01
13296         0x33F0          TIFF image data, big-endian, offset of first image directory: 8
```

展開する。

```bash
$ binwalk --dd ".*" steg01.jpg
```

展開した画像を見ると、フラグが書かれていた。

<!-- flag{L3t_m3_in} -->
