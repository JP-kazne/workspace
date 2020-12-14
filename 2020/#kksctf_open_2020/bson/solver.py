import bson
from bson.codec_options import CodecOptions

codec_options = CodecOptions(unicode_decode_error_handler='ignore')
s = b'\x45\x00\x00\x00\x0b'+b'\x82\xa3\x6b\x65\x79\x5c\xa4\x66\x6c\x61\x67\xdc\x00\x31\x37\x37\x2f\x27\x36\x2f\x6c\x32\x03\x35\x2f\x03\x3f\x6c\x6c\x30\x03\x3e\x29\x28\x03\x34\x3d\x2a\x6f\x03\x25\x33\x29\x03\x28\x2e\x35\x39\x38\x03\x31\x6f\x2f\x2f\x1c\x3b\x39\x03\x2c\x3d\x3f\x37\x21'+b'\x00'
bson_obj = bson.decode_iter(s,codec_options=codec_options)
for item in bson_obj:
    try:
        print(item)
    except Exception as e:
        pass