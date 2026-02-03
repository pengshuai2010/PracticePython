from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # are the candidates positive numbers?
        # will there be duplicates in the candidates?
        # can a number in candidates be used more than once? 
        # will candidates be empty?
        solutions = []
        self._dfs(candidates, 0, [], target, solutions)
        return solutions

    def _dfs(self, candidates, start, partial, remaining, solutions):
        if remaining <= 0:
            if remaining == 0:
                solutions.append(list(partial))
            return
        for i in range(start, len(candidates)):
            partial.append(candidates[i])
            self._dfs(candidates, i, partial, remaining - candidates[i], solutions)
            partial.pop()
