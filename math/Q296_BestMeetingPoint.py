from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        col_coords = []
        row_coords = []
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    row_coords.append(i)
        for j in range(num_cols):
            for i in range(num_rows):
                if grid[i][j] == 1:
                    col_coords.append(j)

        def min_1D_distance(coords):
            # In the odd case, the median is at len(cords) // 2.
            # In the even case, we don't need to actually calculate the median.
            # For the purpose of calculating min distance sum, any point between the two center points works.
            # Think of [0, 2, 5, 8], any point between 2 and 5 (inclusive) would have the same min distance sum.
            median = coords[len(coords) // 2]
            # Alternatively, write sum(abs(coord - median) for coord in coords)
            # However in an interview setting, a for loop shows more clarity
            distance_sum = 0
            for coord in coords:
                distance_sum += abs(coord - median)
            return distance_sum

        def min_1D_distance(coords):
            # Actually to get the min distance sum, there is no need to calculate the median
            left = 0
            right = len(coords) - 1
            distance_sum = 0
            while left < right:
                distance_sum += coords[right] - coords[left]
                left += 1
                right -= 1
            return distance_sum

        row_distance_sum = min_1D_distance(row_coords)
        col_distance_sum = min_1D_distance(col_coords)
        return row_distance_sum + col_distance_sum
