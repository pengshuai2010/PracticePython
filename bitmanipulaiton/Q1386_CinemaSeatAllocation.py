from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # use bit manipulation
        row_map = defaultdict(int)
        num_cols = 10
        LEFT = 0b1111 << 5
        MIDDLE = 0b1111 << 3
        RIGHT = 0b1111 << 1
        for row, column in reservedSeats:
            seats = row_map[row]
            seats |= 1 << (num_cols - column)
            row_map[row] = seats
        num_groups = 0
        # Why not for i in range(1, n + 1)?
        # Because it would be highly inefficient if the rows are sparse,
        # Note the constraint 1 <= n <= 10^9.
        for seats in row_map.values():
            left_seats_free = seats & LEFT == 0
            middle_seats_free = seats & MIDDLE == 0
            right_seats_free = seats & RIGHT == 0
            if left_seats_free:
                num_groups += 1
                if right_seats_free:
                    num_groups += 1
            elif middle_seats_free or right_seats_free:
                num_groups += 1
        num_groups += (n - len(row_map)) * 2
        return num_groups