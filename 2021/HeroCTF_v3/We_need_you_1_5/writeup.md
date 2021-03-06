# Writeup

MEMファイルが与えられるので、Volatilityを使って解析する。

```
For this first step, find the name of the PC!
```

とあるので、PC名を探す。

```bash
$ vol.py -f capture.mem imageinfo

          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                          KDBG : 0x82780c28L

$ vol.py -f capture.mem --kdbg=0x82780c28 --profile=Win7SP1x86 hivelist
Volatility Foundation Volatility Framework 2.6.1
Virtual    Physical   Name
---------- ---------- ----
0x8941a2c0 0x2d58d2c0 \REGISTRY\MACHINE\SYSTEM

$ vol.py -f capture.mem --kdbg=0x82780c28 --profile=Win7SP1x86 printkey -o 0x8941a2c0 -K 'ControlSet001\Control\ComputerName\ComputerName'
Volatility Foundation Volatility Framework 2.6.1
Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \REGISTRY\MACHINE\SYSTEM
Key name: ComputerName (S)
Last updated: 2021-04-19 17:00:09 UTC+0000

Subkeys:

Values:
REG_SZ                        : (S) mnmsrvc
REG_SZ        ComputerName    : (S) KANNIBAL
```

PC名は`KANNIBAL`であることが分かった。

[参考]

* [Volatility/Retrieve-hostname](https://www.aldeid.com/wiki/Volatility/Retrieve-hostname)

<!-- Hero{KANNIBAL} -->
