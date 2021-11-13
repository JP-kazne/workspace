from Crypto.Util.number import *

exec(open('cry-sweet-curve/parameters.txt').read())

_lambda = (((y_Q - y_P) % p) * pow((x_Q - x_P), -1, p)) % p
x_R = (pow(_lambda, 2, p) - x_P - x_Q ) % p
print(long_to_bytes(x_R))
