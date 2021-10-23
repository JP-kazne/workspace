# Writeup

バイナリファイルが与えられる。Ghidraで解析したところ、main関数は以下のようになっていた。

```c
undefined8 main(void)

{
  long lVar1;
  long in_FS_OFFSET;
  byte local_238 [32];
  long local_218;
  int local_210;
  short local_20c;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  lVar1 = 0;
  do {
    if ((&DAT_00102008)[lVar1] != 0) {
      local_238[lVar1] = (&DAT_00102008)[lVar1] ^ 0x5a;
    }
    lVar1 = lVar1 + 1;
  } while (lVar1 != 0x1f);
  local_238[30] = 0;
  puts("What is the best and sp00kiest breakfast cereal?");
  __printf_chk(1,&DAT_001020ad,"Please enter the passphrase: ");
  __isoc99_scanf(&DAT_001020ad,&local_218);
  if (((local_218 == 0x68632d746e753063) && (local_210 == 0x6c756330)) && (local_20c == 0x61)) {
    puts((char *)local_238);
  }
  else {
    puts("notflag{you-guessed-it---this-is-not-the-flag}");
  }
  if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
```

`local_238`にフラグがあると予想し、`DAT_00102008`と`0x5a`のXORをとってみると、フラグが得られた。

```c
    if ((&DAT_00102008)[lVar1] != 0) {
      local_238[lVar1] = (&DAT_00102008)[lVar1] ^ 0x5a;
    }

        puts((char *)local_238);
```

```python
from pwn import *

dat = b'\x3c\x36\x3b\x3d\x21\x39\x6a\x2f\x34\x2e\x77\x39\x32\x6a\x39\x2f\x36\x3b\x77\x39\x3f\x28\x3f\x3b\x36\x77\x1c\x0e\x0d\x27\x00\x00'

print(xor(dat, b'\x5a'))
```

```bash
$ python3 solver.py
b'flag{c0unt-ch0cula-cereal-FTW}ZZ'
```

<!-- flag{c0unt-ch0cula-cereal-FTW} -->
