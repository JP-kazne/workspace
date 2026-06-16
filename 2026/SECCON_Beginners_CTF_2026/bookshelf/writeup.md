# Writeup

FLAG が関係する箇所は `app/books/[id]/page.tsx` ファイルの以下の記述。

```
  {
    id: "2",
    title: "Flight Book",
    author: "Bob",
    description: "Notes about modern React rendering.",
    rating: 5,
    internalNote: process.env.FLAG ?? "ctf4b{dummy_flag}",
  },
```

http://bookshelf.beginners.seccon.games:33456/books/2 を開いて、開発者ツールで `ctf4b` を検索すると、フラグを発見できた。

```
ctf4b{r5c_pr0p5_4r3_n0t_s3cr3t}
```
