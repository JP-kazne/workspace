

# This file was *autogenerated* from the file solver.sage
from sage.all_cmdline import *   # import sage library

_sage_const_5001 = Integer(5001); _sage_const_6 = Integer(6); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1)
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

io = remote('crypto.chal.csaw.io', _sage_const_5001 )
for _ in range(_sage_const_6 ):
    io.recvuntil('mean?\r\n')
    morse_code = io.recvline().strip().decode('utf-8').split(' /')

    char = ''
    for mc in morse_code:
        char_code = ''
        for m in mc.split(' '):
            char_code += morsetab[m]
        char += chr(int(char_code))

    dec = base64.b64decode(char).decode('utf-8')
    e,c,N = _sage_const_0 ,_sage_const_0 ,_sage_const_0 
    exec(dec)
    dec = long_to_bytes(c**(_sage_const_1 /e)).decode('utf-8')
    dec = codecs.decode(dec, 'rot13')
    print('send : ', dec)
    io.sendline(dec)

io.interactive()

