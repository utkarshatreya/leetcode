
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        dp = [0] * (budget + 1)

        min_price = min(price for factor, price in items)

        for factor, price in items:

            # Count free items
            count = 0
            for f, p in items:
                if f % factor == 0:
                    count += 1

            # 0/1 Knapsack
            for j in range(budget, price - 1, -1):
                dp[j] = max(
                    dp[j],
                    dp[j - price] + count
                )

        # Calculate maximum answer
        ans = 0

        for j in range(budget + 1):
            extra = (budget - j) // min_price
            ans = max(ans, dp[j] + extra)

        return ans
