enc = b'\x0cYUV\x02\x13\x16\x1a\x01\x04\x05C\x00\twcx|z(((%.)=K%(>'
enc1 = b'\x0bPPS\r\x0b\x02\x0f\x12\r\x03_G\t\x08yb}v+--*+*8=W,>'
enc2 = b'\x07A[\x06\\\r\x15\t\x04\x07\x18VG]U]@\x02\x08&9&%\' 41".;'

x = "hjlgyjgyj10hadanvbwdmkw00OUONBADANKHM;IMMBMZCNihaillm"

flag = ''
rand_i = 0
for idx, e in enumerate(enc):
    if idx == 0:
        rand_i = e
    else:
        flag += chr(ord(x[rand_i]) ^ e)
        rand_i = (rand_i + 1) % 79
print(f'GrabCON{{{flag}}}')
