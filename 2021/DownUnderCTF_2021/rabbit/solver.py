import bz2
import zipfile
import lzma
import gzip
import os

with open('flag', 'wb') as tmp:
    f = open('flag.txt', 'rb').read()
    tmp.write(f)

while True:
    sign = b''
    with open('flag', 'rb') as tmp:
        sign = tmp.read()[:4]

    if sign == b'BZh9':
        with bz2.open('flag', 'rb') as f, open('tmp', 'wb') as tmp:
            tmp.write(f.read())
        os.system('rm flag')
        os.system('mv tmp flag')
    elif sign == b'PK\x03\x04':
        with zipfile.ZipFile('flag') as f:
            f.extractall('./tmp')
        os.system('rm flag')
        os.system('mv tmp/flag.txt flag')
        os.system('rm -rf tmp')
    elif sign == b'\xfd7zX':
        with lzma.open('flag', 'rb') as f, open('tmp', 'wb') as tmp:
            tmp.write(f.read())
        os.system('rm flag')
        os.system('mv tmp flag')
    elif sign == b'\x1f\x8b\x08\x08':
        with gzip.open('flag', mode='rb') as f, open('tmp', 'wb') as tmp:
            tmp.write(f.read())
        os.system('rm flag')
        os.system('mv tmp flag')
    else:
        print(sign)
        break
