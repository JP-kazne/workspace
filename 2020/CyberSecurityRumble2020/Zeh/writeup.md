# Writeup

以下のプログラムが与えられる。

```c
#include <stdio.h>
#include <stdlib.h>
#include "fahne.h"

#define Hauptroutine main
#define nichts void
#define Ganzzahl int
#define schleife(n) for (Ganzzahl i = n; i--;)
#define bitrverschieb(n, m) (n) >> (m)
#define diskreteAddition(n, m) (n) ^ (m)
#define wenn if
#define ansonsten else
#define Zeichen char
#define Zeiger *
#define Referenz &
#define Ausgabe(s) puts(s)
#define FormatAusgabe printf
#define FormatEingabe scanf
#define Zufall rand()
#define istgleich =
#define gleichbedeutend ==

nichts Hauptroutine(nichts) {
    Ganzzahl i istgleich Zufall;
    Ganzzahl k istgleich 13;
    Ganzzahl e;
    Ganzzahl Zeiger p istgleich Referenz i;

    FormatAusgabe("%d\n", i);
    fflush(stdout);
    FormatEingabe("%d %d", Referenz k, Referenz e);

    schleife(7)
        k istgleich bitrverschieb(Zeiger p, k % 3);

    k istgleich diskreteAddition(k, e);

    wenn(k gleichbedeutend 53225)
        Ausgabe(Fahne);
    ansonsten
        Ausgabe("War wohl nichts!");
}
```

`#define`によって関数名が書き換わっていて分かりづらいので元に戻してみる。

```c
#include <stdio.h>
#include <stdlib.h>
#include "fahne.h"

#define forloop(n) for (int i = n; i--;)
#define rightshift(n, m) (n) >> (m)
#define xor(n, m) (n) ^ (m)

void main(void) {
    int i = rand();
    int k = 13;
    int e;
    int * p = & i;

    printf("%d\n", i);
    fflush(stdout);
    scanf("%d %d", & k, & e);

    forloop(7)
        k = rightshift(* p, k % 3);

    k = xor(k, e);

    if(k == 53225)
        puts(Fahne);
    else
        puts("War wohl void!");
}
```

処理の流れは以下の通り。

1. ![i](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+i) をprintf

1. ![e,k](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+e%2Ck) を入力

1. ![k = (*p) \gg (k \mod 3)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+k+%3D+%28%2Ap%29+%5Cgg+%28k+%5Cmod+3%29) を7回

1. ![53325 = k \oplus e](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+53325+%3D+k+%5Coplus+e)

`nc`してみると常に`1804289383`が返ってくるので`i`は固定っぽい。

```bash
$ nc chal.cybersecurityrumble.de 65123
1804289383
```

最終的に k = 53225 になるように逆算していけば良さそう。

(3)式で、何回ループを回しても *p 自体は変化しないので、k は *p を 0,1,2右シフトした3通りのパターンのいずれかになる。

| シフト | *p         |
| --- | ---------- |
| 0   | 1804289383 |
| 1   | 902144691  |
| 2   | 451072345  |

そして、それぞれに対して k = 53225 となる e を計算すると次のようになる。

![*p \oplus e =53225 \Leftrightarrow e = *p \oplus 53225](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%2Ap+%5Coplus+e+%3D53225+%5CLeftrightarrow+e+%3D+%2Ap+%5Coplus+53225)

* [競技プログラミングにおけるXORのTips](https://qiita.com/kuuso1/items/778acaa7011d98a3ff3a)


| シフト | *p         | e          |
| --- | ---------- | ---------- |
| 0   | 1804289383 | 1804307086 |
| 1   | 902144691  | 902131034  |
| 2   | 451072345  | 451026608  |

よって、`0 1804307086`, `0 902131034`, `0 451026608`のいずれかは k = 53225 になるはずである。

```bash
$ nc chal.cybersecurityrumble.de 65123                       
1804289383                    
0 1804307086 
```

<!-- CSR{RUECKWARTSINGENEUREN}  -->