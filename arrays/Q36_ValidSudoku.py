from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # clarify: valid input? empty list, null?
        # Do we need to verify if the board contain anything other than '0' - '9'?
        n = 9
        subboard_length = 3
        for i in range(n):
            if not self.is_row_valid(board, i):
                return False
        for i in range(n):
            if not self.is_col_valid(board, i, n):
                return False
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                if not self.is_subboard_valid(board, i, j, n, subboard_length):
                    return False
        return True

    def is_row_valid(self, board: List[List[str]], row: int) -> bool:
        num_set = set()
        for cell in board[row]:
            if cell == ".":
                continue
            if cell in num_set:
                return False
            num_set.add(cell)
        return True

    def is_col_valid(self, board: List[List[str]], col: int, num_rows) -> bool:
        num_set = set()
        for row in range(num_rows):
            cell = board[row][col]
            if cell == ".":
                continue
            if cell in num_set:
                return False
            num_set.add(cell)
        return True

    def is_subboard_valid(self, board: List[List[str]], row: int, col: int, length: int, subboard_length: int) -> bool:
        num_set = set()
        for i in range(row, row + subboard_length):
            for j in range(col, col + subboard_length):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in num_set:
                    return False
                num_set.add(cell)
        return True
