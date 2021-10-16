# Writeup

`pcap`ファイルが与えられる。中身を見ると、BLE通信のパケットキャプチャであった。

`Prepare Write Request` の `value, offset`を抜き出してみると以下のようになった。

```
b'1koZPp9re_VJzEU_DNnsSv5xj8QUOWtdL3fjd_lLJCLUbcMc4CQHyAlFH' 1
b'SstG2T3VOeBzXuf7vbe5ZYHfmgZ_EVviRH6LbkgVfCUKnD' 11
b'LjULhLkhPILFXBR3FtcsOWxvKn1prtZfd0g' 11
b'1U90zDT0mZ' 48
b'W1Gm0ANaYQTl0u9TVlrNxttweVQ8B6v' 16
b'HoUBRagyMy6BY78x' 30
b'6C0DIbIdPm_' 16
b'HqrgItMkQddlD_' 33
b'_' 30
b'pcTNrWo' 1
b'xFpT' 11
b'h7x04fO4Crt' 33
b'0Sp07t0p' 50
b'ie3' 11
b'uQY_I7gx5' 16
b'_J' 16
b'is' 17
b'bauRW6' 20
b'D8_' 22
b'bQC2r2zh0l' 35
b'keO' 50
b't1zUg' 3
b'h}q' 55
b'guw4QHt' 35
b'rr' 41
b'3t' 50
b'f{jtE' 4
b'j' 31
b'o1' 6
b'b' 6
b'3' 50
b'\n' 57
b'_SEA' 35
b'y' 27
b'4' 25
b'4' 22
b'A' 41
b't' 11
b'd' 23
b'U' 8
b's' 33
b'4sip' 36
b'k' 38
b'_' 39
```

また、`Read Response`は以下の値になっていた。

```
b'pbctf{REDACTEDREDACTEDREDACTEDREDACTEDREDACTEDREDACTEDRE}\n\x00\x00\x00\x00\x00\x00'
```

フラグの長さが57であることと、`b'\n' 57`に着目し、offsetの値だけずらして上書きしていったところ、フラグが得られた。

```py
from scapy.all import *
from pwn import *

f = rdpcap('btle.pcap')
data = list(b'\x00'*64)
for packets in f:
    if packets.haslayer(ATT_Prepare_Write_Request):
        value = packets[ATT_Prepare_Write_Request].data
        offset = packets[ATT_Prepare_Write_Request].offset
        for idx, v in enumerate(value):
            data[offset + idx] = v
print(bytes(data))
```

<!-- pbctf{b1Ue_te3Th_is_ba4d_4_y0u_jUs7_4sk_HAr0lD_b1U3tO07h} -->
