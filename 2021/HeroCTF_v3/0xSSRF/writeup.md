# Writeup

指定されたページにアクセスするとフォームが表示される。試しにアドレスを入力すると、そのアドレスへのリンクが表示された。

![](img/2021-04-25-16-13-28.png)

また、ページ内にある http://chall1.heroctf.fr:3000/flag のリンクを踏むと以下のメッセージが表示される。

![](img/2021-04-25-16-12-08.png)

内部から　http://chall1.heroctf.fr:3000/flag へアクセスさせれば良さそうだが、そのまま入力してみても`Sorry, the host is too long.`と表示されてしまう。

![](img/2021-04-25-16-15-04.png)

ホスト名を短くしつつ、http://chall1.heroctf.fr:3000/flag へアクセスさせる必要がある。

`locathost`や`127.0.0.1`は対策されていて、`Are you trying to hack me ?`と表示されてしまう。

![](img/2021-04-25-16-22-11.png)

そこで、 http://0:3000/flag としたところ、フラグが得られた。

![](img/2021-04-25-16-23-21.png)

<!-- Hero{cl4ssic_SSRF_byP4pass_251094} -->

[参考]

* [SSRF (Server Side Request Forgery)](https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery)
