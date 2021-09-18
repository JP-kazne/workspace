# Writeup

pcapファイルが与えられるので、wiresharkで解析する。

異常値を出しているのはDevice7であることが周囲との比較でわかった。

![](img/2021-09-12-23-07-00.png)

Object Nameを調べたところ、`Sensor_12345`だったので、これがフラグである。

<!-- flag{Sensor_12345} -->
