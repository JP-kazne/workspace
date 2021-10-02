# Writeup

バイナリファイルが与えられる。Ghidraで解析する。

main関数は以下のようになっていた。

```c
undefined8 main(void)

{
  size_t sVar1;
  undefined8 uVar2;
  long in_FS_OFFSET;
  int local_6c;
  char local_68 [72];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  printf("flag? ");
  fgets(local_68,0x46,stdin);
  local_6c = 0;
  do {
    sVar1 = strlen(local_68);
    if (sVar1 - 1 <= (ulong)(long)local_6c) {
      puts("correct!");
      uVar2 = 0;
LAB_00101231:
      if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
        __stack_chk_fail();
      }
      return uVar2;
    }
    if (local_68[local_6c] != flag[local_6c * 2]) {
      puts("wrong!");
      uVar2 = 0xffffffff;
      goto LAB_00101231;
    }
    local_6c = local_6c + 1;
  } while( true );
}
```

`flag`配列の中身を見ると、フラグがそのまま格納されていた。

```
                             DAT_00102008                                    XREF[3]:     main:001011d0(*), 
                                                                                          main:001011e1(R), 00104050(*)  
        00102008 44              ??         44h    D
        00102009 00              ??         00h
        0010200a 55              ??         55h    U
        0010200b 00              ??         00h
        0010200c 43              ??         43h    C
        0010200d 00              ??         00h
        0010200e 54              ??         54h    T
        0010200f 00              ??         00h
        00102010 46              ??         46h    F
        00102011 00              ??         00h
        00102012 7b              ??         7Bh    {
        00102013 00              ??         00h
        00102014 73              ??         73h    s
        00102015 00              ??         00h
        00102016 74              ??         74h    t
        00102017 00              ??         00h
        00102018 72              ??         72h    r
        00102019 00              ??         00h
        0010201a 69              ??         69h    i
        0010201b 00              ??         00h
        0010201c 6e              ??         6Eh    n
        0010201d 00              ??         00h
        0010201e 67              ??         67h    g
        0010201f 00              ??         00h
        00102020 65              ??         65h    e
        00102021 00              ??         00h
        00102022 6e              ??         6Eh    n
        00102023 00              ??         00h
        00102024 74              ??         74h    t
        00102025 00              ??         00h
        00102026 5f              ??         5Fh    _
        00102027 00              ??         00h
        00102028 73              ??         73h    s
        00102029 00              ??         00h
        0010202a 74              ??         74h    t
        0010202b 00              ??         00h
        0010202c 72              ??         72h    r
        0010202d 00              ??         00h
        0010202e 69              ??         69h    i
        0010202f 00              ??         00h
        00102030 6e              ??         6Eh    n
        00102031 00              ??         00h
        00102032 67              ??         67h    g
        00102033 00              ??         00h
        00102034 73              ??         73h    s
        00102035 00              ??         00h
        00102036 5f              ??         5Fh    _
        00102037 00              ??         00h
        00102038 73              ??         73h    s
        00102039 00              ??         00h
        0010203a 74              ??         74h    t
        0010203b 00              ??         00h
        0010203c 72              ??         72h    r
        0010203d 00              ??         00h
        0010203e 69              ??         69h    i
        0010203f 00              ??         00h
        00102040 6e              ??         6Eh    n
        00102041 00              ??         00h
        00102042 67              ??         67h    g
        00102043 00              ??         00h
        00102044 7d              ??         7Dh    }
        00102045 00              ??         00h
```

<!-- DUCTF{stringent_strings_string} -->
