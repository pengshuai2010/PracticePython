import math
from typing import List
from functools import lru_cache

class Solution:

    # Top down traverse.
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # will triangle be empty?
        min_sum = math.inf
        # Traverse. The time complexity is O(2^n), because at each element there are 2 choices, so the total number of
        # paths is 2 * 2 * 2 ... * 2 = 2^n where n is the number of rows in the triangle.
        def helper(row: int, col: int, path_sum: int) -> None:
            nonlocal min_sum
            if row == len(triangle):
                min_sum = min(min_sum, path_sum)
                return
            path_sum += triangle[row][col]
            helper(row + 1, col, path_sum)
            helper(row + 1, col + 1, path_sum)

        helper(0, 0, 0)
        return int(min_sum)

    # Bottom up. Divide and conquer.
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # will triangle be empty?

        # Time complexity is O(2^n)
        def helper(row: int, col: int) -> int:
            if row == len(triangle):
                return 0
            left_result = helper(row + 1, col)
            right_result = helper(row + 1, col + 1)
            return min(left_result, right_result) + triangle[row][col]

        return helper(0, 0)

    # bottom up with memoization
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # will triangle be empty?

        @lru_cache
        def helper(row: int, col: int) -> int:
            if row == len(triangle):
                return 0
            left_result = helper(row + 1, col)
            right_result = helper(row + 1, col + 1)
            return min(left_result, right_result) + triangle[row][col]

        return helper(0, 0)
