# Writeup

実行ファイルが与えられる。

```bash
$ file v1
v1: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e40523fb4944d772c6ef146eaeda09acbdf6cea0, for GNU/Linux 3.2.0, not stripped
```

Ghidraで解析したところ、`v1`という実行ファイルは`v2`という実行ファイルをダウンロードしてくるものだと分かった。

```c
undefined8 main(void)
{
  long lVar1;
  FILE *__stream;
  
  lVar1 = curl_easy_init();
  printf("Updating to version %s...\n",&DAT_00102008);
  if (lVar1 != 0) {
    __stream = fopen("v2","wb");
    curl_easy_setopt(lVar1,0x2712,"http://147.182.172.217:42100/v2",0x2712);
    curl_easy_setopt(lVar1,0x4e2b,0,0x4e2b);
    curl_easy_setopt(lVar1,0x2711,__stream,0x2711);
    curl_easy_perform(lVar1);
    curl_easy_cleanup(lVar1);
    fclose(__stream);
  }
  printf("Updated to version %s.\n",&DAT_00102008);
  return 0;
}
```

`v2` -> `v3` -> ... と続いていくので、二分探索でどこまで続くのか調べたところ、

`v133791021`まで続くことが分かった。

```py
import requests

session = requests.Session()

min = 100000000
max = 1000000000
mid = lambda a,b : (a+b)//2
pointer = 0

while True:
    if pointer == mid(min,max):
        print(pointer)
        break
    pointer = mid(min,max)
    r = session.get(f'http://147.182.172.217:42100/v{pointer}')
    if r.text == 'version not found':
        max = pointer
    else :
        min = pointer
```

http://147.182.172.217:42100/v133791021 にアクセスしてダウンロードした実行ファイルに対して`strings`コマンドを実行したところ、フラグが得られた。

```
$ strings flag | grep flag
flag{h0w_l0ng_wher3_y0u_g0ne_f0r_3910512832}
flag.c
```

<!-- flag{h0w_l0ng_wher3_y0u_g0ne_f0r_3910512832} -->
