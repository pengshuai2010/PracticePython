from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n > 0?
        # order of returned values?
        expression = []
        solutions = []
        self._helper(expression, 0, 0, n, solutions)
        return solutions

    def _helper(self, expression: list[str], left_count: int, right_count: int, n:int, solutions: [str]) -> None:
        # When left_count == n and right_count == n, we have found a solution.
        if left_count == n and right_count == n:
            solutions.append("".join(expression))
            return
        # an expression is valid if we scan through the expression, and find
        # (1) number of left parentheses <= number of right parentheses is always true at any point of the expression
        # (2) At the end of the expression, number of left parentheses == number of right parentheses

        # At each step, we can either add a "(" or a ")".
        if left_count < n:
            expression.append("(")
            self._helper(expression, left_count + 1, right_count, n, solutions)
            expression.pop()
        if right_count < left_count:
            expression.append(")")
            self._helper(expression, left_count, right_count + 1, n, solutions)
            expression.pop()