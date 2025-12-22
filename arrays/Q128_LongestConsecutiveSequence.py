from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in numbers:
            # Check if the number is the first of the streak and only expand in increasing direction
            # so that we don't duplicate the work
            if num - 1 in numbers:
                continue
            current_streak = 1
            right = num + 1
            while right in numbers:
                current_streak += 1
                right += 1
            longest = max(longest, current_streak)
        return longest