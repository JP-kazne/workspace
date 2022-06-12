# Writeup

以下のプログラムが与えられる。

```py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import isPrime
from secret import FLAG, key
import os


def main():
    while True:
        print('----- Menu -----')
        print('1. Encrypt command')
        print('2. Execute encrypted command')
        print('3. Exit')
        select = int(input('> '))

        if select == 1:
            encrypt()
        elif select == 2:
            execute()
        elif select == 3:
            break
        else:
            pass

        print()


def encrypt():
    print('Available commands: fizzbuzz, primes, getflag')
    cmd = input('> ').encode()

    if cmd not in [b'fizzbuzz', b'primes', b'getflag']:
        print('unknown command')
        return

    if b'getflag' in cmd:
        print('this command is for admin')
        return

    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(pad(cmd, 16))
    print(f'Encrypted command: {(iv+enc).hex()}')


def execute():
    inp = bytes.fromhex(input('Encrypted command> '))
    iv, enc = inp[:16], inp[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        cmd = unpad(cipher.decrypt(enc), 16)
        if cmd == b'fizzbuzz':
            fizzbuzz()
        elif cmd == b'primes':
            primes()
        elif cmd == b'getflag':
            getflag()
    except ValueError:
        pass


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


def primes():
    for i in range(1, 101):
        if isPrime(i):
            print(i)


def getflag():
    print(FLAG)


if __name__ == '__main__':
    main()
```

`1. Encrypt`では、AES-CBCモードでコマンドを暗号化する。暗号文の先頭は`iv`がそのまま入っている。(`print(f'Encrypted command: {(iv+enc).hex()}')`)

`2. Execute`では、暗号化されたコマンドを復号して、それを実行する。

`2. Execute`のときに、復号結果が`getflag`になるような暗号文を与えることができればフラグが得られる。

AES-CBCモードで暗号化されたコマンドを、Bit-Flipping Attack で改ざんすることにより、`getflag`の暗号文を求めることができる。

`pad()`でパディングが付与されていることに気を付ける。

```py
from pwn import *
from Crypto.Util.Padding import pad

def flip(d:bytes, offset:int, src:str, dst:str):
    src, dst = pad(src.encode(), 16), pad(dst.encode(), 16)
    assert len(src) == len(dst)
    d = bytearray(d)
    for i in range(len(src)):
        d[offset+i] = d[offset+i] ^ src[i] ^ dst[i]
    return bytes(d)

io = remote('command.quals.beginners.seccon.jp', 5555)

io.recvuntil('> ')
io.sendline('1')
io.recvuntil('> ')
io.sendline('fizzbuzz')
io.recvuntil('Encrypted command: ')

d = bytes.fromhex(io.recvline().strip().decode())
d = flip(d, 0, 'fizzbuzz', 'getflag')

io.recvuntil('> ')
io.sendline('2')
io.sendline(d.hex())

flag = io.recvline().decode()
print(flag)
```

<!-- ctf4b{b1tfl1pfl4ppers} -->
