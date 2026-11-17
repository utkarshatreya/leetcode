
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Step 1: Precompute cost for every substring
        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):

            # Find all proper divisors
            divisors = [
                d for d in range(1, length)
                if length % d == 0
            ]

            for start in range(n - length + 1):
                end = start + length - 1

                for d in divisors:
                    changes = 0
                    group_size = length // d

                    # Check each group
                    for r in range(d):
                        for t in range(group_size // 2):
                            left = start + r + t * d
                            right = start + r + (group_size - 1 - t) * d

                            if s[left] != s[right]:
                                changes += 1

                    cost[start][end] = min(
                        cost[start][end], changes
                    )

        # Step 2: Dynamic Programming
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):

                for j in range(2 * (p - 1), i - 1):

                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
