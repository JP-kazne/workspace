"""
flag_translated = flag_bin.translate(str.maketrans({"0": trans_0, "1": trans_1})) # flag_bin の 0, 1 を別の文字に置き換える
"""

from pwn import *
from Crypto.Util.number import *

io = remote('01-translator.challenges.beginners.seccon.jp','9999')
io.sendlineafter("translations for 0> ", "0"*16)
io.sendlineafter("translations for 1> ", "0"*15 + "1"*1)
io.recvuntil("ct: ")
ct = io.recvall().decode()
split_ct = [ct[x:x+32] for x in range(0, len(ct), 32)]
print(split_ct)

"""
e.g.)
split_ct = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb", ..., "..._____padding"]
"""

pattern = dict()
_bin = []
for s in split_ct:
    if s not in pattern and len(pattern) < 2: # ignore padding
        pattern[s] = 1 - len(pattern) # The first pattern is "1", second one is "0"
    if s in pattern:
        _bin.append(str(pattern[s]))

print(long_to_bytes(int(''.join(_bin), 2)))

# ctf4b{n0w_y0u'r3_4_b1n4r13n}
