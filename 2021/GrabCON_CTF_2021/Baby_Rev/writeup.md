# Writeup

実行ファイルが与えられる。

Ghidraで解析したところ、main関数内は以下のようになっていた。

```
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined main()
             undefined         AL:1           <RETURN>
             undefined8        Stack[-0x10]:8 local_10                                XREF[2]:     00101193(W), 
                                                                                                   00101197(R)  
             undefined8        Stack[-0x18]:8 local_18                                XREF[2]:     00101179(W), 
                                                                                                   0010117d(R)  
             undefined8        Stack[-0x20]:8 local_20                                XREF[2]:     0010115f(W), 
                                                                                                   00101163(R)  
             undefined4        Stack[-0x24]:4 local_24                                XREF[1]:     001011a0(W)  
             undefined4        Stack[-0x28]:4 local_28                                XREF[1]:     00101186(W)  
             undefined4        Stack[-0x2c]:4 local_2c                                XREF[1]:     0010116c(W)  
             undefined4        Stack[-0x30]:4 local_30                                XREF[1]:     00101152(W)  
             undefined4        Stack[-0x34]:4 local_34                                XREF[2]:     00101143(W), 
                                                                                                   0010114a(R)  
             undefined4        Stack[-0x38]:4 local_38                                XREF[1]:     00101140(W)  
             undefined4        Stack[-0x3c]:4 local_3c                                XREF[2]:     00101131(W), 
                                                                                                   00101138(R)  
                             main                                            XREF[4]:     Entry Point(*), 
                                                                                          _start:00101061(*), 00102028, 
                                                                                          001020b8(*)  
        00101129 f3 0f 1e fa     ENDBR64
        0010112d 55              PUSH       RBP
        0010112e 48 89 e5        MOV        RBP,RSP
        00101131 c7 45 cc        MOV        dword ptr [RBP + local_3c],0x99dfdf8d
                 8d df df 99
        00101138 8b 45 cc        MOV        EAX,dword ptr [RBP + local_3c]
        0010113b 35 ef be        XOR        EAX,0xdeadbeef
                 ad de
        00101140 89 45 d0        MOV        dword ptr [RBP + local_38],EAX
        00101143 c7 45 d4        MOV        dword ptr [RBP + local_34],0x9de2f094
                 94 f0 e2 9d
        0010114a 8b 45 d4        MOV        EAX,dword ptr [RBP + local_34]
        0010114d 35 ef be        XOR        EAX,0xdeadbeef
                 ad de
        00101152 89 45 d8        MOV        dword ptr [RBP + local_30],EAX
        00101155 48 b8 8b        MOV        RAX,0x7830acdf8d8b
                 8d df ac 
                 30 78 00 00
        0010115f 48 89 45 e8     MOV        qword ptr [RBP + local_20],RAX
        00101163 48 8b 45 e8     MOV        RAX,qword ptr [RBP + local_20]
        00101167 35 ef be        XOR        EAX,0xdeadbeef
                 ad de
        0010116c 89 45 dc        MOV        dword ptr [RBP + local_2c],EAX
        0010116f 48 b8 96        MOV        RAX,0x5feadadf96
                 df da ea 
                 5f 00 00 00
        00101179 48 89 45 f0     MOV        qword ptr [RBP + local_18],RAX
        0010117d 48 8b 45 f0     MOV        RAX,qword ptr [RBP + local_18]
        00101181 35 ef be        XOR        EAX,0xdeadbeef
                 ad de
        00101186 89 45 e0        MOV        dword ptr [RBP + local_28],EAX
        00101189 48 b8 df        MOV        RAX,0x5f33b8cb8fdf
                 8f cb b8 
                 33 5f 00 00
        00101193 48 89 45 f8     MOV        qword ptr [RBP + local_10],RAX
        00101197 48 8b 45 f8     MOV        RAX,qword ptr [RBP + local_10]
        0010119b 35 ef be        XOR        EAX,0xdeadbeef
                 ad de
        001011a0 89 45 e4        MOV        dword ptr [RBP + local_24],EAX
        001011a3 b8 00 00        MOV        EAX,0x0
                 00 00
        001011a8 5d              POP        RBP
        001011a9 c3              RET
```

XORしている部分を計算していくとフラグが得られた。

```py
from Crypto.Util.number import *

C = [0x99dfdf8d, 0x9de2f094, 0x7830acdf8d8b, 0x5feadadf96, 0x5f33b8cb8fdf]

flag = b''
for c in C:
    flag += long_to_bytes(c^0xdeadbeef)
print(flag + b'}')
```

<!-- GrabCON{x0rr3d_4way_3ff10} -->