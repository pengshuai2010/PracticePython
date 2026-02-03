from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # will there be "1" in digits? No
        solutions = []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def helper(index: int, partial: [str]):
            if index == len(digits):
                solutions.append("".join(partial))
                return
            for char in mapping[digits[index]]:
                partial.append(char)
                helper(index + 1, partial)
                partial.pop()

        helper(0, [])
        return solutions
