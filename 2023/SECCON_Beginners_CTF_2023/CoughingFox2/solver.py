import math

flag = b'c'
cipher = []
exec(open('CoughingFox2/cipher.txt').read())

def is_square(number: int):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False
    
root_cipher = [0 for _ in range(len(cipher))]

for c in cipher:
    for i in range(len(cipher)):
        if is_square(c-i):
            root_cipher[i] = int(math.sqrt(c-i))
            break

for i, r in enumerate(root_cipher):
    flag += chr(r-flag[i]).encode()

print(flag)

# <!-- ctf4b{hi_b3g1nner!g00d_1uck_4nd_h4ve_fun!!!} -->
