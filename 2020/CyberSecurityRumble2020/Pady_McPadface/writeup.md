Not solved :(

# Try

```bash
$ nc chal.cybersecurityrumble.de 34187 > output.txt
```

コマンドを実行すると以下の出力が得られる。（数字は省略）

```py
#!/usr/bin/env python3
from random import SystemRandom
from config import p,q,e,flag

print("="*50)
print(open(__file__).read())
print("~"*50)

random = SystemRandom()

flag = int.from_bytes(flag,"big")

n = p*q
assert(p<q<2*p)

print(f"{n=}")
print(f"{e=}")

def pad(m):
    assert(m<2**128)
    r = random.randrange(2**(p.bit_length()-65))
    return m+r**2

def encrypt(m):
    return pow(pad(m), e, n)

for i in bin(flag)[2:]:
    print(encrypt(int(i)))

```

```
n=23946008544227658126007712372803958643232141489757386834260550742271224503035086875887914418064683964046938371640632153677880813529023769841157840969433316734058706481517878257755290676559343682013294580085557476138201639446709290119631383493940405818550255561589074538261117055296294434994144540224412018398452371792093095280080422459773487177339595746894989682038387107119249733105558301840478252766907821053044992141741079156669562032221433390029219634673005161989684970682781410366155504440886376453225497112165607897302209008685179791558898003720802478389914297472563728836647547791799771532020349546729665006643
e=65537
11476768266916164235309881869651940983984675977351051488298450585131110601361259097767182157590949077850278997957210418057571307999354160029914789797303064257673407678466176588055141285504559106147929534411017329460235914731370943844688796504720758193546976717119126655806126593345950791534301821557903985493736264684395251936150675286740482526539878961217409934905048447539295655562679224968766009669108468927568770130096114644357525215815012691791276538573769506001550741827885315948422392251512744224078755783499979105637675307490022506657625779496937616765280504522638229224345078966894708384126926174077244882975
6344781982406291229904616097805576891680892322322233659332047813051271052109897033252412538927719488412069758369450241995502516459491473242999017770856786045082580123686511514697479818998491222910687788991281589873507596649734736831753657844561650803919893634314315967644310123683825013046295631859453549892078522986400756535163909207475879084021071358300550008249888124344976827483625126703181222101427358253757725725111508077062593842303282441855876873129588295014017202563048619388174412323763633870647195416100738355366319758548648612458199676439286...
```

* ![n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+n) はおよそ ![2^{2048}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+2%5E%7B2048%7D) くらいで、![p < q < 2*p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p+%3C+q+%3C+2%2Ap) なので ![p,q](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p%2Cq) もおよそ ![2^{1024}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+2%5E%7B1024%7D) くらいである

* ![i](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+i) はバイナリの要素なので 0 か 1 である

![c](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c) が ![(r^2)^e \mod n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%28r%5E2%29%5Ee+%5Cmod+n) と ![(1+r^2)^e \mod n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%281%2Br%5E2%29%5Ee+%5Cmod+n) のどちらなのか見分けられれば良いと思ったが、方法が思いつかなかった。

# Solution

**[Writeup]**

* https://ctftime.org/writeup/24770

![(r^2)^e = (r^e)^2 \equiv c \mod n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%28r%5E2%29%5Ee+%3D+%28r%5Ee%29%5E2+%5Cequiv+c+%5Cmod+n) と変形し、![c](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c) が ![n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+n) を法とする**平方剰余**であるかを調べればよい。

> **平方剰余**
>
> 整数 ![q](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+q) が ![N](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+N) を法として平方数に合同であるとき、 ![q](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+q) は ![N](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+N) を法とする平方剰余という。
>
> ![_{}^{\exists}x$ s.t. $x^2 \equiv q \mod N](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+_%7B%7D%5E%7B%5Cexists%7Dx%24+s.t.+%24x%5E2+%5Cequiv+q+%5Cmod+N)
> ![\Leftrightarrow q : N](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5CLeftrightarrow+q+%3A+N) を法とする平方剰余

![q](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+q) が ![N](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+N) の平方剰余かどうかを次の記号を使って表す。

> **ルジャンドル記号**
>
> ![(\frac{q}{N})=\begin{cases}
1 & (q \is \a \quadratic \residue \modulo N)\\ 
-1 & (\otherwise)
\end{cases}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%28%5Cfrac%7Bq%7D%7BN%7D%29%3D%5Cbegin%7Bcases%7D%0A1+%26+%28q+%5Cis+%5Ca+%5Cquadratic+%5Cresidue+%5Cmodulo+N%29%5C%5C+%0A-1+%26+%28%5Cotherwise%29%0A%5Cend%7Bcases%7D)

また、以下の法則が成り立つ。(証明略)

> 異なる奇素数 ![p,q](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p%2Cq) に対して、
> * ![(\frac{q}{p})(\frac{p}{q}) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%28%5Cfrac%7Bq%7D%7Bp%7D%29%28%5Cfrac%7Bp%7D%7Bq%7D%29+%3D+%28-1%29%5E%7B%5Cfrac%7Bp-1%7D%7B2%7D%5Ccdot%5Cfrac%7Bq-1%7D%7B2%7D%7D)
>
> 奇素数 ![p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p) に対して、
> * ![(\frac{-1}{p}) = (-1)^{\frac{p-1}{2}}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%28%5Cfrac%7B-1%7D%7Bp%7D%29+%3D+%28-1%29%5E%7B%5Cfrac%7Bp-1%7D%7B2%7D%7D)
> * ![(\frac{2}{p}) = (-1)^{\frac{p^2-1}{8}}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%28%5Cfrac%7B2%7D%7Bp%7D%29+%3D+%28-1%29%5E%7B%5Cfrac%7Bp%5E2-1%7D%7B8%7D%7D)
>
> ![a,b](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+a%2Cb) が ![p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p) と互いに素なとき
> * ![(\frac{ab}{p}) = (\frac{a}{p})(\frac{b}{p})](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%28%5Cfrac%7Bab%7D%7Bp%7D%29+%3D+%28%5Cfrac%7Ba%7D%7Bp%7D%29%28%5Cfrac%7Bb%7D%7Bp%7D%29)

[定理の説明]

* https://mathtrain.jp/sogohosoku

[プログラム+解説]

* https://tex2e.github.io/blog/crypto/legendre-and-jacobi-symbls

例）13 で割って 6 余る平方数は存在するか？

| ![x](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x)                         | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
| ----------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![x^2 \mod 13](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%5E2+%5Cmod+13) | 0   | 1   | 4   | 9   | 3   | 12  | 10  | 10  | 12  | 3   | 9   | 4   | 1   |

![\begin{eqnarray}
\begin{split}
(\frac{6}{13}) &= (\frac{2}{13})(\frac{3}{13}) \\
&= (-1)^{\frac{13^2-1}{8}}\cdot(-1)^{\frac{13-1}{2}\cdot\frac{3-1}{2}}\cdot(\frac{13}{3})\\
&= (-1)^{21}\cdot(-1)^{6\cdot1}\cdot(\frac{1}{3})\\
&= (-1)\cdot1\cdot1\\
&= -1
\end{split}
\end{eqnarray}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%7D%0A%5Cbegin%7Bsplit%7D%0A%28%5Cfrac%7B6%7D%7B13%7D%29+%26%3D+%28%5Cfrac%7B2%7D%7B13%7D%29%28%5Cfrac%7B3%7D%7B13%7D%29+%5C%5C%0A%26%3D+%28-1%29%5E%7B%5Cfrac%7B13%5E2-1%7D%7B8%7D%7D%5Ccdot%28-1%29%5E%7B%5Cfrac%7B13-1%7D%7B2%7D%5Ccdot%5Cfrac%7B3-1%7D%7B2%7D%7D%5Ccdot%28%5Cfrac%7B13%7D%7B3%7D%29%5C%5C%0A%26%3D+%28-1%29%5E%7B21%7D%5Ccdot%28-1%29%5E%7B6%5Ccdot1%7D%5Ccdot%28%5Cfrac%7B1%7D%7B3%7D%29%5C%5C%0A%26%3D+%28-1%29%5Ccdot1%5Ccdot1%5C%5C%0A%26%3D+-1%0A%5Cend%7Bsplit%7D%0A%5Cend%7Beqnarray%7D)

各定理を用いて存在しないと判定できる。

平方剰余の判定にはSageMathの`kronecker`関数を用いた。

`solver.sage`

```py
from pwn import *
from Crypto.Util.number import long_to_bytes

n=23946008544227658126007712372803958643232141489757386834260550742271224503035086875887914418064683964046938371640632153677880813529023769841157840969433316734058706481517878257755290676559343682013294580085557476138201639446709290119631383493940405818550255561589074538261117055296294434994144540224412018398452371792093095280080422459773487177339595746894989682038387107119249733105558301840478252766907821053044992141741079156669562032221433390029219634673005161989684970682781410366155504440886376453225497112165607897302209008685179791558898003720802478389914297472563728836647547791799771532020349546729665006643

HOST = 'chal.cybersecurityrumble.de'
PORT = 34187
L = 263 # number of bits to retrieve

sols = [0 for _ in range(L)]
for i in range(10):
    r = remote(HOST,PORT)
    res = r.recvall().split(b"\n")
    cs = []
    for l in res:
        try:
            cs.append(int(l))
        except:
            pass
    assert len(cs) == L
    for j,c in enumerate(cs):
        if kronecker(c,n) == -1:
            sols[j] = 1
    print( long_to_bytes( int("".join(map(str,sols)),2)).decode("utf-8") )
```

[参考]

* https://ctftime.org/writeup/24770

![r](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+r)の値によっては、![(1+r^2)^e \mod n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%281%2Br%5E2%29%5Ee+%5Cmod+n)が平方剰余であると判定される可能性があるので、複数回試行して絞り込む必要がある。

<!-- CSR{c0nstruCt1ng_squ4re_r3sIdues} -->