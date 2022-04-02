def xor(a:bytes, b:bytes) -> bytes:
    return bytes(i^j for i, j in zip(a, b))

S = [None]*4
R = [None]*4
Share = [None]*5

S[0] = b'LINECTF{'

with open('./Share1', 'rb') as f:
    Share[1] = f.read()

with open('./Share4', 'rb') as f:
    Share[4] = f.read()

# solve using S[0]
R[0] = xor(S[0], Share[1][0:8])
R[3] = xor(S[0], Share[4][24:32])
# solve using R[0]
S[3] = xor(R[0], Share[4][0:8])
# solve using R[3]
S[2] = xor(R[3], Share[1][24:32])
# solve using S[3]
R[2] = xor(S[3], Share[1][16:24])
# solve using S[2]
R[1] = xor(S[2], Share[4][8:16])
# solve using R[2]
S[1] = xor(R[2], Share[4][16:24])
print(b''.join(S) + b''.join(R))
