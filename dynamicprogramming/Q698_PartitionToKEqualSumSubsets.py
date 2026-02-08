from functools import lru_cache
from typing import List


class Solution:

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        used = [False] * len(nums)
        nums.sort()
        memo = dict()

        # use tuple as key for memoization
        def helper(index, remaining, count) -> bool:
            if count == k - 1:
                # we have found a solution
                return True
            if remaining == 0:
                # we have found one set, now move on to the next set
                return helper(0, target, count + 1)
            if remaining < 0:
                return False
            key = tuple(used)
            if key in memo:
                return memo[key]
            for i in range(index, len(nums)):
                # nums has been sorted in ascending order, so if nums[i] is greater than remaining,
                # there is no need to try this and the rest
                if nums[i] > remaining:
                    break
                if used[i]:
                    continue
                used[i] = True
                result = helper(i + 1, remaining - nums[i], count)
                memo[tuple(used)] = result
                if result:
                    return True
                used[i] = False
            return False

        return helper(0, target, 0)

    def canPartitionKSubsets_dfs(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        used = [False] * len(nums)
        nums.sort()

        # we cannot simply add @lru_cache here, because the input arguments doesn't capture
        # the state of the recurision, i.e. used, which is a list and unhashable.
        # We would have to use a hashable form, e.g. a string or tuple
        def helper(index, remaining, count) -> bool:
            if count == k - 1:
                # we have found a solution
                return True
            if remaining == 0:
                # we have found one set, now move on to the next set
                return helper(0, target, count + 1)
            if remaining < 0:
                return False
            for i in range(index, len(nums)):
                # nums has been sorted in ascending order, so if nums[i] is greater than remaining,
                # there is no need to try this and the rest
                if nums[i] > remaining:
                    break
                if used[i]:
                    continue
                used[i] = True
                if helper(i + 1, remaining - nums[i], count):
                    return True
                used[i] = False
            return False

        return helper(0, target, 0)

