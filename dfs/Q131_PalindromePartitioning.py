from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Time complexity is O(n * 2^n) because there are 2^n answers in the worst case, and it take O(n) to construct one answer.
        solutions = []

        def helper(start: int, partial: [str]) -> None:
            if start == len(s):
                solutions.append(list(partial))
                return
            for end in range(start + 1, len(s) + 1):  # end is exclustive, so it must be able to reach len(s)
                if is_palindrome(s[start: end]):
                    partial.append(s[start: end])
                    helper(end, partial)
                    partial.pop()

        def is_palindrome(value):
            return s == s[::-1]

        helper(0, [])
        return solutions
