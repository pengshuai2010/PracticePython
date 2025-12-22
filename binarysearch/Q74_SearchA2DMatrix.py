from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # will the matrix be empty?
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        start = 0
        end = num_rows * num_cols - 1
        while start + 1 < end:
            mid = (start + end) // 2 # must use integer divide for index arithmetics
            i = mid // num_cols # must use integer divide for index arithmetics
            j = mid % num_cols
            mid_value = matrix[i][j]
            if mid_value < target:
                start = mid
            elif mid_value > target:
                end = mid
            else:
                return True
        if matrix[start // num_cols][start % num_cols] == target or matrix[end // num_cols][end % num_cols] == target:
            return True
        return False