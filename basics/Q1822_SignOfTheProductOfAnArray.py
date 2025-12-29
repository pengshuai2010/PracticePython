from typing import List, Callable


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -sign
        return sign
# [1, 0]
# [1, -1]
# [-1, -1]

def at_least_one_upper(s: str) -> bool:
    return any(c.isupper() for c in s)

def at_least_one_digit(s: str) -> bool:
    return any(c.isdigit() for c in s)

def apply_rule(fn: Callable[[str], bool], s: str) -> bool:
    return fn(s)

if __name__ == '__main__':
    print(apply_rule(at_least_one_upper, "Abc"))
    print(apply_rule(at_least_one_digit, "Abc"))
    print(apply_rule(at_least_one_digit, "Ab2"))