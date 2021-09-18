from scapy.all import *
import scapy.contrib.modbus as mb

pcap = rdpcap('modbus.pcap')
flag = ''
for pkt in pcap:
    src = pkt[IP].src
    if mb.ModbusADUResponse in pkt and src == '238.0.0.6':
        flag += chr(pkt[IP].registerVal[0])
print(flag)
