from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # assuming s is not empty and wordDict is not empty
        n = len(s)
        dictionary = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dictionary:
                    dp[i] = True
                    break
        return dp[n]
