# Writeup

実行ファイルが与えられる。

```bash
$ file polymer/polymer
polymer/polymer: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=9cf7ed0dba73b90a2bdbb26b98a17c11c528fe14, for GNU/Linux 3.2.0, stripped
```

stringsコマンドを使ったところ、ダミーのフラグが表示される。

```bash
$ strings polymer/polymer | grep flag{ | head -n 10
according to all known laws of aviation, there is no way a flag{n0t_th3_fl4g_l0l} should be able to flag{n0t_th3_fl4g_l0l}
the flag{n0t_th3_fl4g_l0l} of course, flies anyway because flag{n0t_th3_fl4g_l0l} don't care what humans think is impossible.
flag{n0t_th3_fl4g_l0l} breakfast is ready!
flag{n0t_th3_fl4g_l0l}
flag{n0t_th3_fl4g_l0l} can't.
ma! flag{n0t_th3_fl4g_l0l} got a thing going here.
flag{n0t_th3_fl4g_l0l} flag{n0t_th3_fl4g_l0l} told you, stop flag{n0t_th3_fl4g_l0l} in the house!
hey, flag{n0t_th3_fl4g_l0l}
three days college. i'm glad flag{n0t_th3_fl4g_l0l} took a day and hitchhiked around the hive.
hi, flag{n0t_th3_fl4g_l0l} artie, growing a mustache? looks good.
```

ダミーでないフラグを探したところ、見つけることができた。

```bash
$ strings polymer/polymer | grep -E "flag{[^n]"
mr. flag{n0t_th3_fl4g_l0l} flag{n0t_th3_fl4g_l0l} i'll ask you what the real flag is flag{ju5t_4n0th3r_str1ng5_pr0bl3m_0159394921} think we'd all like to know.
```

<!-- flag{ju5t_4n0th3r_str1ng5_pr0bl3m_0159394921} -->
