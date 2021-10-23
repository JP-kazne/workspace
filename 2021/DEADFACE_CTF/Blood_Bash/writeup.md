# Writeup

ユーザー名とパスワード、ホスト名が与えられているので、SSHでログインする。

ログインに成功したら、`flag1.txt`を読み出す。

```bash
$ ssh bloodbash.deadface.io -p 22 -l bl0ody_mary
bl0ody_mary@bloodbash.deadface.io's password:
bl0ody_mary@a21018531e01:~$ find -name 'flag1.txt'
./Documents/flag1.txt
bl0ody_mary@a21018531e01:~$ cat ./Documents/flag1.txt
flag{cd134eb8fbd794d4065dcd7cfa7efa6f3ff111fe}
```

<!-- flag{cd134eb8fbd794d4065dcd7cfa7efa6f3ff111fe} -->
