class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers length >= 2? guaranteed a solution?
        # can the same element be used twice?
        l = 0
        r = len(numbers) -1
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        raise ValueError("no solution")