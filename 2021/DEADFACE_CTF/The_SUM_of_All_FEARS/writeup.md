# Writeup

パケットキャプチャファイルをWiresharkで開き、`.exe`, `.bin`で検索して見つかったTCPストリームを追跡する。

ファイルが保存できるので、それぞれ保存してmd5sumコマンドでハッシュ値を調べる。

```
$ md5sum pcap.exe
9cb9b11484369b95ce35904c691a5b28  pcap.exe
```

```
$ md5sum pcap.bin
4da8e81ee5b08777871e347a6b296953  pcap.bin
```

<!-- flag{9cb9b11484369b95ce35904c691a5b28|4da8e81ee5b08777871e347a6b296953} -->
