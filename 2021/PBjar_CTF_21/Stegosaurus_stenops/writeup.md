# Writeup

画像ファイルが与えられる。

```
some unusually large rock
```

という問題文から、`rockyou.txt`で辞書攻撃すればよいと推測した。

実行したところ、`snowflake`がパスワードであることが分かった。

```bash
$ python3 -m stegcracker stegosaurus.jpg ~/john/rockyou.txt
StegCracker 2.1.0 - (https://github.com/Paradoxis/StegCracker)
Copyright (c) 2021 - Luke Paris (Paradoxis)

StegCracker has been retired following the release of StegSeek, which
will blast through the rockyou.txt wordlist within 1.9 second as opposed
to StegCracker which takes ~5 hours.

StegSeek can be found at: https://github.com/RickdeJager/stegseek

Counting lines in wordlist..
Attacking file 'stegosaurus.jpg' with wordlist '/home/ubuntu/john/rockyou.txt'..
Successfully cracked file with password: snowflake
Tried 1747 passwords
Your file has been written to: stegosaurus.jpg.out
snowflake
```

<!-- flag{ungulatus_better_than_stenops} -->
