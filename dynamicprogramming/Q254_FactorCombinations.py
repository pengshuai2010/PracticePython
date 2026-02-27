from typing import List
import math


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result: List[List[int]] = []
        if n <= 3:
            return result

        def helper(num: int, start: int, path: [int]) -> None:
            # Only need to try factors up to sqrt(num). Why? This way we don't have duplicates like [4, 6] and [6, 4]
            # Why isqrt(num) instead of int(sqrt(num)) ? Because isqrt is precise, and int(sqrt(num)) could have
            # floating point rounding error.
            limit = math.isqrt(num)
            for factor in range(start, limit + 1):
                if num % factor != 0:
                    continue
                quotient = num // factor
                # all the numbers in path are less than or equal to start
                result.append(path + [factor, quotient])
                # keep factoring quotient
                path.append(factor)
                helper(quotient, factor, path)
                path.pop()

        helper(n, 2, [])

        return result