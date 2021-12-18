import string

LOWER_A2Z = string.ascii_lowercase
LOWER_Z2A = LOWER_A2Z[::-1]

d = 'yzhsufo_rh_nb_uze_wdziu'
m = ''
for c in d:
    index = LOWER_A2Z.find(c)
    if index != -1:
        m += LOWER_Z2A[index]
    else:
        m += c
print(m)
