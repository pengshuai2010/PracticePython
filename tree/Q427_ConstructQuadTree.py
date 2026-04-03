from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    # The time complexity is O(n^2) where n = len(grid)
    # the algorithm would go over every cell, and there are n^2 cells. However, it would also need to merge cells into
    # grid of 4 cells, then merge grid of 4 cells into grid of 16 cells, ..., until there is only 1 grid. So there would
    # be n^2 + n^2/4 + n^2/16 + ... + 1 operations of creating a grid. So in total, the number of operations is
    # n^2 * (1 + 1/4 + 1/16 + ... + 1/(2^k)) where k = log(n).
    # 1/4 + 1/16 + 1/64 + ... is bounded by 3/4. So the total is less than 7/4 * n^2. Hence O(n^2).
    def construct(self, grid: List[List[int]]) -> 'Node':
        # Assuming grid is not empty
        # can I assume the size of grid is 2^n?
        n = len(grid)

        def helper(start_row, start_col, size):
            if size == 1:
                return Node(bool(grid[start_row][start_col]), True, None, None, None, None)
            new_size = size // 2
            top_left = helper(start_row, start_col, new_size)
            top_right = helper(start_row, start_col + new_size, new_size)
            bottom_left = helper(start_row + new_size, start_col, new_size)
            bottom_right = helper(start_row + new_size, start_col + new_size, new_size)
            all_leaves = top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf
            same_value = top_left.val == top_right.val == bottom_left.val == bottom_right.val
            if all_leaves and same_value:
                return Node(top_left.val, True, None, None, None, None)
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)

        return helper(0, 0, n)