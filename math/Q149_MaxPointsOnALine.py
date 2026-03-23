import math
from collections import Counter
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Will there be dulicates in the input?
        # Will there be at least two points?

        def normalize_slope(dx, dy):
            # Don't forget the horizontal line and vertical line cases.
            if dy == 0:
                slope = (1, 0)
            elif dx == 0:
                slope = (0, 1)
            else:
                # Need to normalize, e.g. reducing 8/6 to 4/3.
                g = math.gcd(abs(dx), abs(dy))
                dx = dx // g
                dy = dy // g
                if dx < 0:
                    dx, dy = -dx, -dy
                slope = (dx, dy)
            return slope

        max_points = 0
        for i in range(len(points)):
            anchor = points[i]
            # The key is the slope a line represented as a rational number, e.g. 4/3.
            # Not using a float point number because of precision issues.
            # The value is the number of points on the same line with the anchor, not including the anchor itself
            slopes = Counter()
            for j in range(i + 1, len(points)):
                other = points[j]
                dx = anchor[0] - other[0]
                dy = anchor[1] - other[1]
                slope = normalize_slope(dx, dy)
                slopes[slope] += 1
            for value in slopes.values():
                max_points = max(max_points, value)
        return max_points + 1 # we need to include the anchor itself

