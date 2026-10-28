class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j] stores all possible XOR values
        # for paths ending at cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]

                # Come from the top
                if i > 0:
                    for x in dp[i - 1][j]:
                        dp[i][j].add(x ^ value)

                # Come from the left
                if j > 0:
                    for x in dp[i][j - 1]:
                        dp[i][j].add(x ^ value)

        return min(dp[m - 1][n - 1])