from Crypto.Util.number import long_to_bytes

f = open('knapsack/output.txt', 'r').read().replace(':','=')
b = []
c = 0
exec(f)

def create_matrix(c,pk):
    matrix_size = len(pk) + 1
    M = [
        [0 for _ in range(matrix_size)] for _ in range(matrix_size)
    ]

    for i in range(matrix_size - 1):
        M[i][0] = pk[i]
        M[i][i+1] = 2
        M[matrix_size - 1][i+1] = -1

    M[matrix_size - 1][0] = - c
    return M

def is_valid_vector(b):
    if b[0] != 0:
        return False
    for i, x in enumerate(b):
        if i != 0 and abs(x) != 1:
            return False
    return True

lllm = Matrix(ZZ, create_matrix(c,b)).LLL()

flag_vecs = []
for basis in lllm:
    if is_valid_vector(basis):
        flag_vecs.append(basis)

for v in flag_vecs:
    flag = ""
    for _bit in reversed(v[1:]):
        c = ("1" if _bit == 1 else "0")
        flag = c + flag

    print(long_to_bytes(int(flag, 2)))