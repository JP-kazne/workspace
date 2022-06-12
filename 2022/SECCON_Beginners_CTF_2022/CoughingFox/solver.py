cipher = []
exec(open('output.txt').read())

square_numbers = [(i, i**2) for i in range(0x20, 0x7F + len(cipher))]

flag_dec = [0 for _ in range(len(cipher))]
for c in cipher:
    diff = [abs(c-n2) for _, n2 in square_numbers]
    idx = min(diff)
    flag_dec[idx] = square_numbers[diff.index(idx)]

flag = ''
for idx, f in enumerate(flag_dec):
    n, _ = f
    flag += chr(n-idx)

print(flag)
