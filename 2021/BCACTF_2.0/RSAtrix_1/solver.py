from Crypto.Util.number import *

p = 35953130875571662629774552621633952493346190947047
q = 68201352784431955275947627343562102980308744031461
n = p * q
e = 3

ct = 1879922562037963072325125556499104095457740584077567873217970367519076380025989311243974742849996920
d = pow(e,-1,(p-1)*(q-1))
mt = pow(ct,d,n)
print(long_to_bytes(mt))
