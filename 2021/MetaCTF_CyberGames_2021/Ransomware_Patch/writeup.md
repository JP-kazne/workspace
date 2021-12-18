# Writeup

zipファイルが与えられたので、情報を見てみる。

```bash
$ zipinfo ransomware-final.zip
Archive:  ransomware-final.zip
Zip file size: 17227 bytes, number of entries: 17
drwx---     6.3 fat        0 bx stor 21-Nov-29 17:40 AES/
-rw-a--     6.3 fat    19017 Bx defN 21-Nov-29 16:35 AES/aes.c
-rw-a--     6.3 fat     2790 Bx defN 21-Nov-29 16:35 AES/aes.h
-rw-a--     6.3 fat      184 Bx defN 21-Nov-29 16:35 AES/aes.hpp
-rw-a--     6.3 fat      366 Bx defN 21-Nov-29 16:35 AES/CMakeLists.txt
-rw-a--     6.3 fat     2050 Bx defN 21-Nov-29 16:35 AES/conanfile.py
-rw-a--     6.3 fat      279 Bx defN 21-Nov-29 16:35 AES/library.json
-rw-a--     6.3 fat      557 Bx defN 21-Nov-29 16:35 AES/library.properties
-rw-a--     6.3 fat     1261 Bx defN 21-Dec-03 12:29 AES/Makefile
-rw-a--     6.3 fat     4783 Bx defN 21-Nov-29 16:35 AES/README.md
-rw-a--     6.3 fat    15539 Bx defN 21-Nov-29 16:35 AES/test.c
-rw-a--     6.3 fat       37 Bx stor 21-Nov-29 16:35 AES/test.cpp
drwx---     6.3 fat        0 bx stor 21-Nov-29 16:43 AES/test_package/
-rw-a--     6.3 fat      313 Bx defN 21-Nov-29 16:35 AES/test_package/CMakeLists.txt
-rw-a--     6.3 fat      413 Bx defN 21-Nov-29 16:35 AES/test_package/conanfile.py
-rw-a--     6.3 fat     1211 Bx defN 21-Nov-29 16:35 AES/unlicense.txt
-rw-a--     6.3 fat       33 Bx stor 21-Nov-29 16:38 key
17 files, 48833 bytes uncompressed, 14623 bytes compressed:  70.1%
```

`key`というファイルの中身が分かればよいが、暗号付きzipなので開けない。

AES関連のファイルで既知平文攻撃してみる。

`aes.c`は https://github.com/kokke/tiny-AES-c/blob/master/aes.c から取ってきた。

```bash
$ pkcrack -C ransomware-final.zip -c AES/aes.c -P AES.zip -p AES/aes.c -d decrypt.zip
Files read. Starting stage 1 on Sun Dec  5 22:02:10 2021
Generating 1st generation of possible key2_5535 values...done.
Found 4194304 possible key2-values.
Now we're trying to reduce these...
Done. Left with 1886 possible Values. bestOffset is 24.
Stage 1 completed. Starting stage 2 on Sun Dec  5 22:02:16 2021
Ta-daaaaa! key0=a71f05f4, key1=18438c7b, key2=1cf62c29
Probabilistic test succeeded for 5516 bytes.
Stage 2 completed. Starting zipdecrypt on Sun Dec  5 22:02:50 2021
Decrypting AES/aes.c (8f8c1547846efccdcf9e7deb)... OK!
Decrypting AES/aes.h (d17bd1e0c5c27683e28eecc2)... OK!
Decrypting AES/aes.hpp (257e198b30d633e1fdb7d2f5)... OK!
Decrypting AES/CMakeLists.txt (0f5897854193720bbaf7bc24)... OK!
Decrypting AES/conanfile.py (cb0efd59736f5c50aa14a265)... OK!
Decrypting AES/library.json (c9a7fb4c9811923bd961d095)... OK!
corrupted size vs. prev_size
[1]    1844 abort      ~/pkcrack-1.2.2/src/pkcrack -C ransomware-final.zip -c AES/aes.c -P AES.zip -
```

pkcrackのdecryptでエラーになったので、`zipdecrypt`を使って実行しなおしてみると復号できた。

```bash
$ ~/pkcrack-1.2.2/src/zipdecrypt a71f05f4 18438c7b 1cf62c29 ransomware-final.zip decrypt.zip
Decrypting AES/aes.c (8f8c1547846efccdcf9e7deb)... OK!
Decrypting AES/aes.h (d17bd1e0c5c27683e28eecc2)... OK!
Decrypting AES/aes.hpp (257e198b30d633e1fdb7d2f5)... OK!
Decrypting AES/CMakeLists.txt (0f5897854193720bbaf7bc24)... OK!
Decrypting AES/conanfile.py (cb0efd59736f5c50aa14a265)... OK!
Decrypting AES/library.json (c9a7fb4c9811923bd961d095)... OK!
Decrypting AES/library.properties (5d7353b0182aca779e38b614)... OK!
Decrypting AES/Makefile (c45df47860c1be4e9ea39486)... OK!
Decrypting AES/README.md (dfdf83ba9b13fa33c9f6f075)... OK!
Decrypting AES/test.c (9b0c44ae4730c3bb7af6513d)... OK!
Decrypting AES/test.cpp (aa2b214dd12bbf37d2c9f5df)... OK!
Decrypting AES/test_package/CMakeLists.txt (2cfaf44fd615a91ed0cffc99)... OK!
Decrypting AES/test_package/conanfile.py (220d1a9f3e9369ba8588d53f)... OK!
Decrypting AES/unlicense.txt (fe9574b917066dc6da212a98)... OK!
Decrypting key (2d861ee2ce494d138a06e453)... OK!
```

`key`にフラグが書かれていた。

<!-- MetaCTF{license_is_hard_to_spell} -->
