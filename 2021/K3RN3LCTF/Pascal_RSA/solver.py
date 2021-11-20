from Crypto.Util.number import *
from tqdm import tqdm

exec(open('challenge.txt').read())

d = 1
for i in tqdm(range(p)):
    d = d ^ 2*d

m = pow(enc, d, N)
print(long_to_bytes(m))