# Writeup

```
⭐🌈🍀 ⭐🌈🦄 ⭐🦄🌈 ⭐🎈🍀 ⭐🦄🌑 ⭐🌈🦄 ⭐🌑🍀 ⭐🦄🍀 ⭐🎈⭐ 🦄🦄 ⭐🦄🎈 ⭐🌑🍀 ⭐🌈🌑 ⭐🌑⭐ ⭐🦄🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄⭐ ⭐🌈🍀 🦄🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🌑🦄 🦄🦄 ⭐🌑🐴 ⭐🌑🦄 ⭐🌈🍀 ⭐🌈🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄🦄 ⭐🌑🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🦄🎈 ⭐🌑🌑 ⭐🎈🦄
```

対象の文字列を見てみると、3つ区切りで8種の文字が使われていることが分かった。

ということは8進数が関連していそうだと推測。

試しにフラグ形式の`sun{}`を8進数に変換してみると

`163 165 156 173 175` となる。

* https://gchq.github.io/CyberChef/#recipe=To_Octal('Space')&input=c3Vue30

絵文字と比べてみると、以下の対応があることが分かった。

| number | emoji |
| ------ | ----- |
| 0      |       |
| 1      | ⭐     |
| 2      |       |
| 3      | 🍀    |
| 4      |       |
| 5      | 🦄    |
| 6      | 🌈    |
| 7      | 🎈    |

```
163 165 156 173 15🌑 165 1🌑3 153 171 55 157 1🌑3 16🌑 1🌑1 15🌑 55 1🌑5 156 1🌑3 157 1🌑🌑 151 156 1🌑7 55 151 163 55 16🌑 15💜 1🌑5 55 1🌑🐴 1🌑5 163 16🌑 55 1🌑5 156 1🌑3 157 1🌑🌑 151 156 1🌑7 55 155 1🌑5 16🌑 15💜 157 1🌑🌑 175
```

残りは総当たりで絞り込んでいく。結果、下のように対応付けると綺麗に英単語が現れる。

| number | emoji |
| ------ | ----- |
| 0      | 💜    |
| 1      | ⭐     |
| 2      | 🐴    |
| 3      | 🍀    |
| 4      | 🌑    |
| 5      | 🦄    |
| 6      | 🌈    |
| 7      | 🎈    |

* [CyberChef-Recipe](https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':'%F0%9F%92%9C'%7D,'0',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%E2%AD%90'%7D,'1',true,true,true,false)Find_/_Replace(%7B'option':'Regex','string':'%F0%9F%90%B4'%7D,'2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%F0%9F%8D%80'%7D,'3',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%F0%9F%8C%91'%7D,'4',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%F0%9F%A6%84'%7D,'5',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%F0%9F%8C%88'%7D,'6',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%F0%9F%8E%88'%7D,'7',true,false,true,false)From_Octal('Space')&input=4q2Q8J%2BMiPCfjYAg4q2Q8J%2BMiPCfpoQg4q2Q8J%2BmhPCfjIgg4q2Q8J%2BOiPCfjYAg4q2Q8J%2BmhPCfjJEg4q2Q8J%2BMiPCfpoQg4q2Q8J%2BMkfCfjYAg4q2Q8J%2BmhPCfjYAg4q2Q8J%2BOiOKtkCDwn6aE8J%2BmhCDirZDwn6aE8J%2BOiCDirZDwn4yR8J%2BNgCDirZDwn4yI8J%2BMkSDirZDwn4yR4q2QIOKtkPCfpoTwn4yRIPCfpoTwn6aEIOKtkPCfjJHwn6aEIOKtkPCfpoTwn4yIIOKtkPCfjJHwn42AIOKtkPCfpoTwn46IIOKtkPCfjJHwn4yRIOKtkPCfpoTirZAg4q2Q8J%2BmhPCfjIgg4q2Q8J%2BMkfCfjogg8J%2BmhPCfpoQg4q2Q8J%2BmhOKtkCDirZDwn4yI8J%2BNgCDwn6aE8J%2BmhCDirZDwn4yI8J%2BMkSDirZDwn6aE8J%2BSnCDirZDwn4yR8J%2BmhCDwn6aE8J%2BmhCDirZDwn4yR8J%2BQtCDirZDwn4yR8J%2BmhCDirZDwn4yI8J%2BNgCDirZDwn4yI8J%2BMkSDwn6aE8J%2BmhCDirZDwn4yR8J%2BmhCDirZDwn6aE8J%2BMiCDirZDwn4yR8J%2BNgCDirZDwn6aE8J%2BOiCDirZDwn4yR8J%2BMkSDirZDwn6aE4q2QIOKtkPCfpoTwn4yIIOKtkPCfjJHwn46IIPCfpoTwn6aEIOKtkPCfpoTwn6aEIOKtkPCfjJHwn6aEIOKtkPCfjIjwn4yRIOKtkPCfpoTwn5KcIOKtkPCfpoTwn46IIOKtkPCfjJHwn4yRIOKtkPCfjojwn6aE)

<!-- sun{lucky-octal-encoding-is-the-best-encoding-method} -->