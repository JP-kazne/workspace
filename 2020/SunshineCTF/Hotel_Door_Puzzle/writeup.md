# Writeup

`file`コマンドでファイルの形式を調べる。

```bash
$ file hotel_key_puzzle 
hotel_key_puzzle: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c4add21a28170d0828bedc432f1ed178007be0d0, for GNU/Linux 3.2.0, not stripped
```

実行してみる。

```bash
$ ./hotel_key_puzzle 
Hotel Orlando Door Puzzle v1
----------------------------
This puzzle, provided by Hotel Orlando, is in place to give the bellhops enough time to get your luggage to you.
We have really slow bellhops and so we had to put a serious _time sink_ in front of you.
Have fun with this puzzle while we get your luggage to you!

	-Hotel Orlando Bellhop and Stalling Service

Your guess, if you would be so kind: 
hoge
Sadly, that is the incorrect key. If you would like, you could also sit in our lobby and wait.
```

正しいkeyを入力すれば良さそうなので、angrを使って調べる。

```py
import angr

p = angr.Project('hotel_key_puzzle')
main_addr = p.loader.main_object.get_symbol('main').rebased_addr
print('main_addr = ',main_addr)
state = p.factory.entry_state()
sim = p.factory.simulation_manager(state)
addr_success = main_addr + (0x22BA-0x221B)
sim.explore(find=addr_success)
if len(sim.found) > 0:
    print(sim.found[0].posix.dumps(0))
```

<!-- sun{b3llh0p5-runn1n6-qu1ckly} -->




