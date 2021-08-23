# Writeup

実行ファイルが与えられる。

```
$ file babyrev
babyrev: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=705028dd88484cf2fab5829c051d5b383a808ae0, for GNU/Linux 3.2.0, not stripped
```

Ghidraで解析する。

```c
undefined8 main(void)

{
  char cVar1;
  int iVar2;
  size_t sVar3;
  undefined8 uVar4;
  long in_FS_OFFSET;
  int local_100;
  int local_fc;
  undefined8 local_f0;
  char local_e8 [64];
  char local_a8 [27];
  undefined auStack141 [37];
  char local_68 [72];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  fgets(local_e8,0x40,stdin);
  sVar3 = strcspn(local_e8,"\n");
  local_e8[sVar3] = '\0';
  sVar3 = strlen(local_e8);
  local_f0 = 7;
  iVar2 = strncmp("corctf{",local_e8,7);
  if (((iVar2 == 0) && (local_e8[sVar3 - 1] == '}')) && (sVar3 == 0x1c)) {
    memcpy(local_a8,local_e8 + local_f0,0x1b - local_f0);
    auStack141[-local_f0] = 0;
    local_100 = 0;
    while( true ) {
      sVar3 = strlen(local_a8);
      if (sVar3 <= (ulong)(long)local_100) break;
      local_fc = local_100 << 2;
      while( true ) {
        cVar1 = is_prime(local_fc);
        if (cVar1 == '\x01') break;
        local_fc = local_fc + 1;
      }
      cVar1 = rot_n((int)local_a8[local_100],local_fc,local_fc);
      local_68[local_100] = cVar1;
      local_100 = local_100 + 1;
    }
    sVar3 = strlen(local_68);
    local_68[sVar3 + 1] = '\0';
    memfrob(check,0x14);
    iVar2 = strcmp(local_68,check);
    if (iVar2 == 0) {
      puts("correct!");
      uVar4 = 0;
    }
    else {
      puts("rev is hard i guess...");
      uVar4 = 1;
    }
  }
  else {
    puts("rev is hard i guess...");
    uVar4 = 1;
  }
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar4;
}


undefined8 is_prime(int param_1)

{
  undefined8 uVar1;
  double dVar2;
  int local_c;
  
  if (param_1 < 2) {
    uVar1 = 0;
  }
  else {
    local_c = 2;
    while (dVar2 = sqrt((double)param_1), local_c <= (int)dVar2) {
      if (param_1 % local_c == 0) {
        return 0;
      }
      local_c = local_c + 1;
    }
    uVar1 = 1;
  }
  return uVar1;
}

char rot_n(char param_1,int param_2)

{
  char *pcVar1;
  
  pcVar1 = strchr(ASCII_UPPER,(int)param_1);
  if (pcVar1 == (char *)0x0) {
    pcVar1 = strchr(ASCII_LOWER,(int)param_1);
    if (pcVar1 != (char *)0x0) {
      param_1 = ASCII_LOWER[(param_1 + -0x61 + param_2) % 0x1a];
    }
  }
  else {
    param_1 = ASCII_UPPER[(param_1 + -0x41 + param_2) % 0x1a];
  }
  return param_1;
}
```

main関数内、以下の比較部分で一致するような文字列を見つければよい。

```c
    memfrob(check,0x14);
    iVar2 = strcmp(local_68,check);
```

`local_68`は以下の手順で生成される。

1. for文のカウンタ(0x00 ~ 0x14)を2ビット左シフトする

1. シフトした値よりも大きく、最も近い素数を求める

1. 入力文字列を上で計算した素数分だけ、ROTNする

    * アルファベットでない場合はROTせず、そのままにする

これが`memfrob(check)`と一致するような文字列を探索するプログラムを実行したところ、フラグが得られた。

```py
from Crypto.Util.number import *
import string

CHAR = string.printable
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase

check = [0x5f,0x40,0x5a,0x15,0x75,0x45,0x62,0x53,0x75,0x46,0x52,0x43,0x5f,0x75,0x50,0x52,0x75,0x5f,0x5c,0x4f]

flag = 'corctf{'
for i,c in enumerate(check):
    c ^= 42 # memfrob
    n = i << 2
    while not isPrime(n):
        n += 1
    if chr(c) not in LOWER+UPPER:
        flag += chr(c)
        continue
    for ch in LOWER+UPPER:
        if ch in LOWER:
            rotn = ord(LOWER[(ord(ch) - 0x61 + n) % 0x1a])
        elif ch in UPPER:
            rotn = ord(UPPER[(ord(ch) - 0x41 + n) % 0x1a])
        if rotn == c:
            flag += ch
            break
flag += '}'
print(flag)
```

<!-- corctf{see?_rEv_aint_so_bad} -->
