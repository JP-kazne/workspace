# Writeup

Firefox のプロファイルが与えられる。

`dctf`でフォルダ内検索をかけると、`logins.json` があったので、ログイン情報を以下のサイトを参考に取り出してみる。

* https://medium.com/geekculture/how-to-hack-firefox-passwords-with-python-a394abf18016

```bash
$ python3.9 firefox_decrypt.py ~/workspace/2022/DCTF_2022/Hidden_Fox/Firefox/            

Website:   https://dctf.dragonsec.si
Username: 'dragonflag'
Password: 'dctf{1_b00km4rk3d_'
```

フラグ文字列の前半部分より、ブックマークが参考になりそうだと推測したので、ブックマーク情報が格納されている `places.sqlite` を以下のサイトを参考に調べてみる。

* https://dayflower.hatenablog.com/entry/20081209/1228790603

```bash
$ sqlite3 Firefox/Profiles/br873ssy.default-release/places.sqlite 
sqlite> SELECT * FROM moz_places;
1|https://support.mozilla.org/products/firefox||gro.allizom.troppus.|0|0|0|140||bew1ljtsvWMG|1|47358327123126||||1
2|https://support.mozilla.org/kb/customize-firefox-controls-buttons-and-toolbars?utm_source=firefox-browser&utm_medium=default-bookmarks&utm_campaign=customize||gro.allizom.troppus.|0|0|0|140||2-8jSXGE10oO|1|47359956450016||||1
3|https://www.mozilla.org/contribute/||gro.allizom.www.|0|0|0|140||P9_q5kTlvFJo|1|47357364218428||||2
4|https://www.mozilla.org/about/||gro.allizom.www.|0|0|0|140||5QcP8AsXsadx|1|47357608426557||||2
5|https://www.mozilla.org/firefox/central/||gro.allizom.www.|0|0|0|140||G9hmLxo6sCFe|1|47359969280417||||2
6|about:blank||.|0|0|0|0||ymJwHGBAObVu|0|175532304468422||||3
7|http://dctf.dragonsec.si/||is.cesnogard.ftcd.|0|0|0|140||ktppGpUqRORF|0|125510471171359||||4
8|http://_th15_p455w0rd}/||}dr0w554p_51ht_.|0|0|0|140||Pwebe5bDioa9|3|125507539440179||||5
```

つなぎ合わせるとフラグが得られる。

<!-- dctf{1_b00km4rk3d__th15_p455w0rd} -->
