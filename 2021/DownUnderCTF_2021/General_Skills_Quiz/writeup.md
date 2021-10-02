# Writeup

`nc pwn-2021.duc.tf 31905`を実行すると以下のように表示された。

```bash
$ nc pwn-2021.duc.tf 31905

Welcome to the DUCTF Classroom! Cyber School is now in session!
Press enter when you are ready to start your 30 seconds timer for the quiz...
Woops the time is always ticking...
Answer this maths question: 1+1=?
```

提示される質問に答えるスクリプトを作成し、実行したところ、フラグが得られた。

```py
from pwn import *
from urllib import parse
import base64
import codecs

io = remote('pwn-2021.duc.tf', 31905)

# Start
io.recvuntil('...')
io.sendline('')
# Q1
io.recvuntil(': ')
eq = io.recvline().decode().replace('=?','').strip()
ans = eval(eq)
io.sendline(str(ans))
# Q2
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = eval(eq)
io.sendline(str(ans))
# Q3
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = int(eq,16)
io.sendline(chr(ans))
# Q4
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = parse.unquote(eq)
io.sendline(ans)
# Q5
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = base64.b64decode(eq)
io.sendline(ans)
# Q6
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = base64.b64encode(eq.encode())
io.sendline(ans)
# Q7
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = codecs.decode(eq,'rot13')
io.sendline(ans)
# Q8
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = codecs.decode(eq,'rot13')
io.sendline(ans)
# Q9
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = eval(eq)
io.sendline(str(ans))
# Q10
io.recvuntil(': ')
eq = io.recvline().decode().strip()
ans = bin(eval(eq))
io.sendline(str(ans))
# Q11
io.recvuntil('?')
io.sendline('DUCTF')

io.interactive()

io.close()
```

```
Bloody Ripper! Here is the grand prize!



   .^.
  (( ))
   |#|_______________________________
   |#||##############################|
   |#||##############################|
   |#||##############################|
   |#||##############################|
   |#||########DOWNUNDERCTF##########|
   |#||########(DUCTF 2021)##########|
   |#||##############################|
   |#||##############################|
   |#||##############################|
   |#||##############################|
   |#|'------------------------------'
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|  DUCTF{you_aced_the_quiz!_have_a_gold_star_champion}
   |#|
   |#|
   |#|
  //|\\
```

<!-- DUCTF{you_aced_the_quiz!_have_a_gold_star_champion} -->
