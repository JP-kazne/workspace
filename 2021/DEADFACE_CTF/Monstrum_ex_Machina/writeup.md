# Writeup

pcapngファイルが与えられる。

検索エンジンで調べた単語を抽出すればよいので、`http.request.method == "GET"`でフィルタリングすると、以下のパケットが見つかった。

![](img/2021-10-16-16-57-42.png)

`Charles Geschickter`と調べていることが分かったので、これがフラグである。

<!-- flag{Charles Geschickter} -->
