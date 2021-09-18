import string
import re

def up(x):
    x = [f"{ord(x[i]) << 1:08b}" for i in range(len(x))]
    return ''.join(x)

def down(x):
    x = ''.join(['1' if x[i] == '0' else '0' for i in range(len(x))])
    return x

def right(x,d):
    x = x[d:] + x[0:d]
    return x

def left(x,d):
    x = right(x,len(x)-d)
    return x[::-1]

def encode(plain):
    d = 24
    x = up(plain)
    x = right(x,d)
    x = down(x)
    x = left(x,d)
    return x

def solver_dict():
    table = {}
    for flag in string.printable:
        table[encode(flag)] = flag
    return table


if __name__ == "__main__":
    encoded = "1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100"
    d = solver_dict()
    encoded = re.findall(r'[0,1]{8}',encoded)
    flag = ''
    for e in encoded:
        flag += d[e]
    print(flag[::-1])
