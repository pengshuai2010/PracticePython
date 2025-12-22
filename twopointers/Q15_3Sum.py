from typing import List

class Solution:
    class Solution:
        def threeSum_dedup(self, nums: List[int]) -> List[List[int]]:
            # nums len > 3? guranteed to have a solution?
            # Will there be duplicate numbers? Yes
            # Duplicates not allowed in solution.
            # Can I modify the input list? i.e. sort it in place.
            # Deduplicate without using a set.
            result = []
            nums.sort()
            for i in range(len(nums) - 2):
                # small optimization
                # target is 0 and nums[i] is the smallest
                if nums[i] > 0:
                    break
                if i > 0 and nums[i] == nums[i - 1]:
                    # dedup
                    continue
                j = i + 1
                k = len(nums) - 1
                target = - nums[i]
                while j < k:
                    total = nums[j] + nums[k]
                    if total < target:
                        j += 1
                    elif total > target:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1  # dedup. handles the case like [-1, -1, 2, 2]
                        k -= 1
            return result


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums len > 3? guranteed to have a solution? 
        # Will there be duplicate numbers? Yes
        # Duplicates not allowed in solution. Throw solutions in a set to deduplicate
        # Can I modify the input list? i.e. sort it in place.
        dedup = set()
        nums.sort()
        for i in range(len(nums) - 2):
            # small optimization
            # target is 0 and nums[i] is the smallest
            if nums[i] > 0: 
                break
            j = i + 1
            k = len(nums) - 1
            target = - nums[i]
            while j < k:
                total = nums[j] + nums[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    dedup.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return [[num1, num2, num3] for num1, num2, num3 in dedup]


