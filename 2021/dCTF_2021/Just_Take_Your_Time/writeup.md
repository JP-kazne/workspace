# Writeup

Pythonプログラムが与えられる。

初めに、ランダムな数字`a`,`b`の乗算結果を求められるので計算する。

```py
a = randint(1000000000000000, 9999999999999999)
b = randint(1000000000000000, 9999999999999999)

print("Show me you are worthy and solve for x! You have one second.")
print("{} * {} = ".format(a, b))

answ, _ = timedInput("> ", timeOut = 1, forcedTimeout = True)

try:
    assert(a*b == int(answ))
except:
    print("You are not worthy!")
    exit(1)
```

2番目に、ランダムな16バイトの`secret`を入力するように求められる。

`secret`は`key`を時刻(1秒単位)、`iv`を`b"00000000"`とした`CFB`モードの`DES3 encryption`が行われる。

```py
key = str(int(time())).zfill(16).encode("utf-8")
secret = token_hex(16)
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
encrypted = cipher.encrypt(secret.encode("utf-8"))
print("You have proven yourself to be capable of taking on the final task. Decrypt this and the flag shall be yours!")
print(encrypted.hex())

start_time = time()
while(time() - start_time < TIMEOUT and guess > 0):
    delta = time() - start_time
    answ, _ = timedInput("> ", timeOut = TIMEOUT + 1 - delta, forcedTimeout = True)

    try:
        assert(secret == answ)
        break
    except:
        if answ != "":
            guess -= 1
            if (guess != 1):
                print("You are wrong. {} guesses remain.".format(guess))
            else:
                print("You are wrong. {} guess remains.".format(guess))

if (secret != answ):
    print("You have been unsuccessful in your quest for the flag.")
else:
    print("Congratulations! Here is your flag.")
    print(flag)
```

`iv`が固定であることから、`key`だけ分かれば`DES3 decryption`できる。

サーバー側の`time()`だけで`key`の計算ができるので、サーバーとのラグを考慮する必要がある。

`DES3 decryption`の結果が16バイトの16進数（`token_hex()`の形式）になっていればよい。

```py
from pwn import *
from time import time
from Crypto.Cipher import DES3

from pwnlib.util.fiddling import xor

io = remote('dctf-chall-just-take-your-time.westeurope.azurecontainer.io', '9999')

io.recvuntil('You have one second.\n')

calc = None
exec('calc = ' + io.recvline().decode('utf-8').split('=')[0])
io.sendline(str(calc))

io.recvuntil('flag shall be yours!\n')
encrypted = bytes.fromhex(io.recvline_regex(r'[0-9a-f]*').decode('utf-8'))

now = int(time())
for i in range(60):
    key = str(now-i).zfill(16).encode("utf-8")
    cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
    decrypted = cipher.decrypt(encrypted)
    if '\\x' not in str(decrypted):
        io.sendline(decrypted)
        print(decrypted, -i)
        break

print(io.recvall())
io.close()
```

<!-- dctf{1t_0n1y_t0Ok_2_d4y5...} -->
