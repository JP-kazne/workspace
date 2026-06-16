# Writeup

> 素数の片方が負の値なのに対し、オイラー関数を(p-1)*(q-1)と計算しているのがポイントだと私は思います。何か exploit の方法はないでしょうか？

この問題の最大の脆弱性は、**$p$ が負の素数であるにもかかわらず、復号鍵 $d$ の計算に用いる「オイラーのトーシェント関数の値」を模した $\phi = (p-1)(q-1)$ が、法 $n$ の下での正しい位数（group order）になっていない点**にあります。

しかし、この「誤った $d$」を用いた復号結果 $m2$ が与えられていることが、逆に $n$ を素因数分解する手がかりとなります。

### Exploit の仕組み

1.  **フェルマーの小定理の適用**
    $m2$ の計算式は $m2 \equiv c^d \pmod n$ です。これは法 $n$ の各因子 $p, q$ についても成り立ちます。
    特に正の素数 $q$ について考えると：
    $m2 \equiv (m1^e)^d \equiv m1^{ed} \pmod q$

2.  **指数の関係**
    スクリプトでは $d \equiv e^{-1} \pmod{(p-1)(q-1)}$ と定義されているため、
    $ed = 1 + k(p-1)(q-1)$ （$k$ は整数）と書けます。

3.  **$m2 \equiv m1 \pmod q$ の証明**
    これを $m2 \equiv m1^{ed} \pmod q$ に代入すると：
    $m2 \equiv m1^{1 + k(p-1)(q-1)} \equiv m1 \cdot (m1^{q-1})^{k(p-1)} \pmod q$
    フェルマーの小定理より $m1^{q-1} \equiv 1 \pmod q$ なので、
    $m2 \equiv m1 \cdot 1^{k(p-1)} \equiv m1 \pmod q$ となります。

4.  **素因数 $q$ の抽出**
    $m1 \equiv m2 \pmod q$ であるということは、$(m1^e) \equiv m2^e \pmod q$ でもあります。
    暗号文 $c$ は $c \equiv m1^e \pmod n$ なので、当然 $c \equiv m1^e \pmod q$ です。
    したがって、以下の関係が導かれます：
    $c \equiv m2^e \pmod q$  $\Rightarrow$  $c - m2^e$ は $q$ の倍数である。

    $n$ も $q$ の倍数であるため、最大公約数（GCD）をとることで $q$ を特定できます：
    $q = \gcd(n, c - m2^e)$


```
ctf4b{of_cours3_n3g4tiv3_numb3rs_4r3_not_prim3_numb3rs}
```
