# Writeup

ユーザー名とパスワード、ホスト名が与えられているので、SSHでログインする。

`*.txt`を探したところ、隠しファイルがあったので中身を見ると、フラグが書かれていた。。

```bash
$ ssh bloodbash.deadface.io -p 22 -l bl0ody_mary
bl0ody_mary@bloodbash.deadface.io's password:
bl0ody_mary@31b9fc17e0e0:~$ find -name '*.txt'
./Documents/flag1.txt
./Documents/.demonne_info.txt
bl0ody_mary@31b9fc17e0e0:~$ cat ./Documents/.demonne_info.txt
flag{a856b162978fe563537c6890cb184c48fc2a018a}
```

<!-- flag{a856b162978fe563537c6890cb184c48fc2a018a} -->
