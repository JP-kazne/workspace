# Writeup

PDFをバイナリエディタで開くと、 "PK ~~~ FLAG.txt" という文字列がある。

この部分のみを抽出して zip として開くと、FLAG.txt を展開して見ることができる。

（標準的なZIPファイルの先頭バイトは、ASCII文字で PK と表示される。）

```
ctf4b{Im_914d_y0u_f0und_thi5_f149}
```

