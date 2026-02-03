from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # will there be duplicates in candidates? Yes.
        # if there could be duplicates, are duplicate solutions allowed? No.
        # is the candidadtes list sorted
        # will candidates list be empty?
        # are the numbers in candidates all positive?
        solutions = []
        candidates.sort()
        self._dfs(candidates, 0, [], target, solutions)
        return solutions

    def _dfs(self, candidates, start, partial, remaining, solutions):
        if remaining <= 0:
            if remaining == 0:
                solutions.append(list(partial))
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            partial.append(candidates[i])
            self._dfs(candidates, i + 1, partial, remaining - candidates[i], solutions)
            partial.pop()