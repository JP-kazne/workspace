# Writeup

netcatすると三目並べが始まるので、勝ち続ければ良さそう。

```
$ nc challs.dvc.tf 6666
Welcome to my TicTacToe game ! Will you be able to beat me 100 times in a row ?
Format your answer like so : "row_number column_number"
--------------------------------------------------
- - -
- - -
- - -
2 2

- - -
- X -
O - -
3 3

O - -
- X -
O - X
2 1

O - O
X X -
O - X
2 3

O - O
X X X
O - X
Well done ! 1/250
```

自動で三目並べを行うプログラムを書く。負けなければよいので、負ける条件を潰していくように書いた。

```py
from pwn import *

class Solver:

    def __init__(self):
        self.io = remote('challs.dvc.tf', 6666)
        self.io.recvlines(3) # discard description
        self.board = [[]]
        self.win = False
        self.end = False

    def _check(self):
        # res = win 1, lose -1

        # Win case
        # check row
        for idx, b in enumerate(self.board):
            if b.count('X') == 2 and b.count('-') == 1:
                return (1, idx+1, b.index('-')+1)
        # check column
        for idx, b in enumerate([[b[i] for b in self.board] for i in range(3)]):
            if b.count('X') == 2 and b.count('-') == 1:
                return (1, b.index('-')+1, idx+1)
        # check corner
        b = [self.board[0][0] ,self.board[1][1] ,self.board[2][2]]
        if b.count('X') == 2 and b.count('-') == 1:
            return (1, b.index('-')+1, b.index('-')+1)
        b = [self.board[0][2], self.board[1][1], self.board[2][0]]
        if b.count('X') == 2 and b.count('-') == 1:
            return (1, b.index('-')+1, 3-b.index('-'))

        # Lose case
        # check row
        for idx, b in enumerate(self.board):
            if b.count('O') == 2 and b.count('-') == 1:
                return (-1, idx+1, b.index('-')+1)
        # check column
        for idx, b in enumerate([[b[i] for b in self.board] for i in range(3)]):
            if b.count('O') == 2 and b.count('-') == 1:
                return (-1, b.index('-')+1, idx+1)
        # check corner
        b = [self.board[0][0] ,self.board[1][1] ,self.board[2][2]]
        if b.count('O') == 2 and b.count('-') == 1:
            return (-1, b.index('-')+1, b.index('-')+1)
        b = [self.board[0][2], self.board[1][1], self.board[2][0]]
        if b.count('O') == 2 and b.count('-') == 1:
            return (-1, b.index('-')+1, 3-b.index('-'))
        
        return (0, 0, 0)

    def _print(self, board):
        print(board[0])
        print(board[1])
        print(board[2])

    def put(self, r, c):
        self.io.sendline(f'{r} {c}')

    def put_center(self):
        if self.board[1][1] == '-':
            self.put(2, 2)
            return True
        return False

    def put_must(self):
        (res, r, c) = self._check()
        if res != 0:
            self.put(r, c)
            if res == 1:
                self.win = True
            return True
        return False

    def prevent_checkmate(self):
        # prevent double checkmate
        if self.board[0][0] == '-':
            if self.board[0][1] == 'O' or self.board[1][0] == 'O':
                self.put(1, 1)
                return True
        if self.board[0][2] == '-':
            if self.board[0][1] == 'O' or self.board[1][2] == 'O':
                self.put(1, 3)
                return True
        if self.board[2][0] == '-':
            if self.board[2][1] == 'O' or self.board[1][0] == 'O':
                self.put(3, 1)
                return True
        if self.board[2][2] == '-':
            if self.board[2][1] == 'O' or self.board[1][2] == 'O':
                self.put(3, 3)
                return True
        return False

    def put_else(self):
        if self.board[0][0] == '-':
            self.put(1, 1)
        elif self.board[0][2] == '-':
            self.put(1, 3)
        elif self.board[2][0] == '-':
            self.put(3, 1)
        elif self.board[2][2] == '-':
            self.put(3, 3)
        elif self.board[0][1] == '-':
            self.put(1, 2)
        elif self.board[1][0] == '-':
            self.put(2, 1)
        elif self.board[1][2] == '-':
            self.put(2, 3)
        elif self.board[2][1] == '-':
            self.put(3, 2)

    def recv_board(self):
        board = []
        while len(board) < 3:
            res = self.io.recvline()
            if len(res) == 7:
                board.append(res)
            elif res != b'\n':
                print(res)
                if b'250/250' in res:
                    self.end = True
        return board

    def solve(self):
        msg = self.recv_board()
        self.board = [line_.decode().split() for line_ in msg]
        # self._print(self.board) # debug
        if self.win:
            self.win = False
            return
        if self.put_center():
            return
        if self.put_must():
            return
        if self.prevent_checkmate():
            return
        self.put_else()
        
s = Solver()
while not s.end:
    s.solve()
```

<!-- dvctf{T1ct4Ct0e_iS_2_EZ} -->
