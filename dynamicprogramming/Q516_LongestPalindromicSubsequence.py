class Solution:

    # Iterative solution
    def longestPalindromeSubseq(self, s: str) -> int:
        # assuming s is not empty
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
            else:
                dp[i][i + 1] = 1
        for k in range(2, n): # k = j - i
            for i in range(0, n - k):
                j = i + k
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]

    # Recursive solution: DFS + memoization
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = dict()
        # assuming s is not empty
        def helper(start, end):
            key = (start, end)
            if key in memo:
                return memo[key]
            if start == end:
                return 1
            if start + 1 == end:
                return 2 if s[start] == s[end] else 1
            if s[start] == s[end]:
                result = helper(start + 1, end - 1) + 2
            else:
                result = max(helper(start, end - 1), helper(start + 1, end))
            memo[key] = result
            return result

        return helper(0, len(s) - 1)