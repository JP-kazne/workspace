# Writeup

ncコマンドを実行すると、質問が表示される。

```bash
$ nc code.deadface.io 50000
DEADFACE gatekeeper: Let us see how good your programming skills are.
If a = 0, b = 1, c = 2, etc.. Tell me what the sum of this word is:

 You have 5 seconds to give me an answer.

Your word is: disagreeable
```

質問に答えるようなスクリプトを作成して実行するとフラグが得られた。

```python
from pwn import *

io = remote('code.deadface.io', 50000)

msg = io.recvuntil('Your word is: ').decode()
print(msg)
word = io.recvline().decode().strip()
print(word)
s = sum([ord(w)-ord('a') for w in word])
io.sendline(str(s))

io.interactive()
```

<!-- flag{d1c037808d23acd0dc0e3b897f344571ddce4b294e742b434888b3d9f69d9944} -->
