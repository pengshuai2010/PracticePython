import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(nums, l, r):
            if l >= r:
                return l, r
            p = random.randint(l, r)
            nums[l], nums[p] = nums[p], nums[l]
            pivot = nums[l]
            lt = l
            i = l
            gt = r
            while i <= gt:
                if nums[i] < pivot:
                    # swap nums[i] and nums[lt]
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    # swap nums[i] and nums[gt]
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            return lt, gt

        def quicksort(nums, s, e):
            if s >= e:
                return
            lt, gt = partition(nums, s, e)
            quicksort(nums, s, lt - 1)
            quicksort(nums, gt + 1, e)

        quicksort(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    nums = [5,2,3,1]
    Solution().sortArray(nums)
    print(nums)
