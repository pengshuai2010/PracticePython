from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force takes O(n^2) time.
        # We can avoid unnecessary calculations through two pointers technique. The idea is to have one pointer
        # starting from the left, another pointer starting from the right. Each time move one pointer. We should
        # move the pointer where the height is the lower of the two, because it is possible that the next one has
        # a higher height which compensates for the decrease in width. Moving the taller line will never help,
        # because the height either stays the same or decrease, and the width definitely decreases.
        # When two lines are of the same height, it won't matter moving which one. Why? Because the onl way that
        # area could increase is when move pointers move to much taller lines (think of [1, 100, 100, 1]).
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return max_area