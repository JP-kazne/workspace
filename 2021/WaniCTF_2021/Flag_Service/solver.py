import base64

d = 'yH8E9m039e1rav+2S/kIX2D8eEJk/Gf5VvsBv7LI//6WwmnffTTHMJqPuZmw7sNbPO9VnxWbP3CK8NcWgmYSwg=='
d = base64.b64decode(d)

def flip(d:bytes, offset:int, src:str, dst:str):
    assert len(src) == len(dst)
    d = bytearray(d)
    for i in range(len(src)):
        d[offset+i] = d[offset+i] ^ ord(src[i]) ^ ord(dst[i])
    return bytes(d)

offset = len('{"admin": ')
d = flip(d, offset, 'false', ' true')
d = base64.b64encode(d)
print(d)
