class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Assuming m > 0, n > 0
        dp = [ [1] * n for _ in range(m)]
        # dp[0][j] = 1 for any j
        # dp[i][0] = 1 for any i
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]