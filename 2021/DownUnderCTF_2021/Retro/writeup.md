# Writeup

画像ファイルが与えられる。`strings`コマンドを実行したところフラグが得られた。

```bash
$ strings og.jpg | grep DUCTF
DUCTF{sicc_paint_skillz!}
                        <dc:creator><rdf:Seq xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:li>DUCTF{sicc_paint_skillz!}</rdf:li></rdf:Seq>
```

<!-- DUCTF{sicc_paint_skillz!} -->
