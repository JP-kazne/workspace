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