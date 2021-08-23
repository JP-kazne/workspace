fib = [1, 1]
for i in range(2, 11):
    fib.append(fib[i - 1] + fib[i - 2])

def f2c(b):
    n = 0
    c = ''
    for i in range(10):
        if b[i] == '1':
            n += fib[10-i]
    c += chr(n)
    return c

with open('flag.enc','r') as f:
    enc = f.read().split(' ')
    dec = ''.join([f2c(e) for e in enc])

print(dec)