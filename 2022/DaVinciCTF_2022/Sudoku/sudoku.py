from __future__ import annotations
from pprint import pformat
from typing import List, Set, Tuple

ROWS = COLS = 9
NUMBERS = [x for x in range(1, 9 + 1)]

class Grid:
    """数独のクイズを表すグリッド"""

    _values: List[List[int]]

    def __init__(self, values: List[List[int]]):
        assert isinstance(values, list)
        assert len(values) == ROWS
        for row in values:
            assert isinstance(row, list)
            assert len(row) == COLS

        self._values = values

    def __hash__(self):
        """hashable 化するための __hash__ 定義

        - set() で利用するため
        """
        return hash(''.join(str(x) for row in self._values for x in row))

    def __str__(self):
        """`print()` で出力されたときの表現を定義する"""
        return '{}(\n{}\n)'.format(type(self).__name__, pformat(self._values))

    def solved(self) -> bool:
        """空セルがなくなったかどうかを判定する"""
        all_values = [x for row in self._values for x in row]
        return 0 not in all_values

    def possible_numbers(self) -> List[Tuple[int, int, List[int]]]:
        """すべての空セルと入りうる数字の組み合わせを全件洗い出す"""
        return [
            (row, col, self._possible_numbers_for_cell(row, col))
            for row, values in enumerate(self._values)
            for col, x in enumerate(values)
            if x == 0
        ]

    def clone_filled(self, row, col, number) -> Grid:
        """特定のセルに指定された値が入った新しい grid を返す"""
        values = [[x for x in row] for row in self._values]
        values[row][col] = number
        return type(self)(values)

    def _possible_numbers_for_cell(self, row, col) -> List[int]:
        row_numbers = [x for x in self._values[row]]
        col_numbers = [row[col] for row in self._values]
        block_numbers = self._block_numbers(row, col)

        return [
            x
            for x in NUMBERS
            if (x not in row_numbers)
            and (x not in col_numbers)
            and (x not in block_numbers)
        ]

    def _block_numbers(self, row, col) -> List[int]:
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        return [
            x
            for row in self._values[row_start : row_start + 3]
            for x in row[col_start : col_start + 3]
        ]

def solve_all(grid: Grid) -> Set[Grid]:
    """指定された数独に対する解を全件返す"""
    solutions = set()

    def _solve(grid: Grid):
        # S4. 空のセルがなくなったら正解として追加
        if grid.solved():
            solutions.add(grid)
            return

        # S1. すべてのセルに対して入りうる数字をリストアップする
        possible_numbers = grid.possible_numbers()

        # S2 + S3. 入りうち数字が最も少ないセルに仮に数字を入れて再帰
        row, col, numbers = min(possible_numbers, key=lambda x: len(x[-1]))

        # S5. 入りうる数字がひとつも無い空のセルがある場合はそのルートは間違いなので終了
        if not numbers:
            return

        for number in numbers:
            next_grid = grid.clone_filled(row, col, number)
            _solve(next_grid)

    _solve(grid)

    return solutions
