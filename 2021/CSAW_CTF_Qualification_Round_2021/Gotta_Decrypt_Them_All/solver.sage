import collections
from pwn import *
import base64
import codecs
from Crypto.Util.number import *

morsetab = collections.OrderedDict([
    ('-----', '0'),
    ('.----', '1'),
    ('..---', '2'),
    ('...--', '3'),
    ('....-', '4'),
    ('.....', '5'),
    ('-....', '6'),
    ('--...', '7'),
    ('---..', '8'),
    ('----.', '9'),
])

io = remote('crypto.chal.csaw.io', 5001)
for _ in range(6):
    io.recvuntil('mean?\r\n')
    morse_code = io.recvline().strip().decode('utf-8').split(' /')

    char = ''
    for mc in morse_code:
        char_code = ''
        for m in mc.split(' '):
            char_code += morsetab[m]
        char += chr(int(char_code))

    dec = base64.b64decode(char).decode('utf-8')
    e,c,N = 0,0,0
    exec(dec)
    dec = long_to_bytes(c^(1/e)).decode('utf-8')
    dec = codecs.decode(dec, 'rot13')
    print('send : ', dec)
    io.sendline(dec)

io.interactive()
