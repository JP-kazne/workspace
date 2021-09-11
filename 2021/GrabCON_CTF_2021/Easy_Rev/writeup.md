# Writeup

実行ファイルが与えられる。

Ghidraで解析したところ、以下の関数が見つかった。

```c
undefined8 FUN_00101277(void)

{
  long in_FS_OFFSET;
  int local_20;
  undefined4 local_1c;
  undefined4 local_18;
  int local_14;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_1c = 0x1466c7;
  local_18 = 0xdeb9d828;
  local_14 = 0x140685;
  puts("Looking for the flag?");
  printf("Enter the key: ");
  __isoc99_scanf(&DAT_0010202f,&local_20);
  if (local_14 == local_20) {
    FUN_001011a9();
  }
  else {
    puts("Wrong! Try Again ...");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

`0x140685 = 1312389`なので、`1312389`と入力するとフラグが得られた。

```bash
$ ./baby_re_2
Looking for the flag?
Enter the key: 1312389
GrabCON{y0u_g0t_it_8bb31}
```

<!-- GrabCON{y0u_g0t_it_8bb31} -->
