# Original : https://github.com/TalaatHarb/ctf-writeups/blob/main/hxpctf2020/nanothorpe/exploit.py
import requests
import base64

from urllib.parse import parse_qsl, unquote_to_bytes, urlencode
from struct import pack, unpack

from nanothorpe.octothorpe import octothorpe

def parse(query_string):
    return dict(parse_qsl(query_string, errors='ignore')), unquote_to_bytes(query_string)

# base_url = 'http://157.90.22.14:8832/'
base_url = 'http://localhost:8832/'

headers = {\
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',\
    'Referer'         : base_url,\
    'Accept'          : '*/*',\
    'Connection'      : 'keep-alive',\
    'Accept-Language' : 'en-US,en;q=0.9'\
}

params1 = {\
    'cmd' : 'ls'\
}

secret_length = 32 # got it by trail and error
r1 = requests.get(base_url + 'api/authorize', headers=headers, params=params1, allow_redirects=False)
signature =  r1.cookies.get('signature')
path_url = r1.next.path_url
args, decoded = parse(path_url[path_url.index('?')+1:])
expiry = r1.next.path_url[path_url.index('=')+1:path_url.index('&')]

# Actual exploit here : manuiplating the signature to allow another command
actual_length = secret_length + len(decoded)
padding = b'\x80' + b'\x00' * ((octothorpe.block_size - 9 - actual_length) % octothorpe.block_size) + (8 * actual_length).to_bytes(8, 'little')
b = b'&cmd=cat+/flag*'
n = actual_length + len(padding)
ha = signature
hb = octothorpe(b, _length=n, _state=bytearray.fromhex(ha)).hexdigest()

old_cmd = {'expiry':expiry,'cmd': (b'ls' + padding)}
new_cmd = {'cmd':(b'cat /flag*')}

old_enc = urlencode(old_cmd)
new_enc = urlencode(new_cmd)

parameters = (old_enc + '&' + new_enc) # parameters = {'expiry':expiry,'cmd':'old_cmd+padding','cmd':'new_cmd'}

cookies2 = {\
    'signature' : hb\
}

# End of trickery
r2 = requests.get(base_url + 'api/run?' + parameters, headers=headers, cookies=cookies2, allow_redirects=False)
status_code = r2.status_code

if status_code != 403 and status_code != 503:
    print(base64.b64decode(r2.json()['stdout']).decode('utf-8').rstrip(), sep='')