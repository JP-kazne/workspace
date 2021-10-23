# Writeup

画像ファイルが与えられる。

steghideを使い、パスワード無しでデータを展開したところ、フラグが書かれたテキストファイルが得られた。

```bash
$ steghide extract -sf bunny.jpg
Enter passphrase:
wrote extracted data to "steganopayload730241.txt".
```

<!-- flag{Carr0t} -->
