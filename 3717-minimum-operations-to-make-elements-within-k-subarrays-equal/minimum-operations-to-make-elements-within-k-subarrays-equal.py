
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.bit[i]
            i -= i & -i
        return ans

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        pos = {v: i + 1 for i, v in enumerate(vals)}

        # Two Fenwick trees:
        # One for frequency, one for sum
        freq = Fenwick(m)
        sums = Fenwick(m)

        total = 0

        # Add first window
        for i in range(x):
            p = pos[nums[i]]
            freq.add(p, 1)
            sums.add(p, nums[i])
            total += nums[i]

        costs = []

        def get_cost():
            # Lower median
            mid_pos = freq.kth((x + 1) // 2)
            median = vals[mid_pos - 1]

            count_left = freq.query(mid_pos)
            sum_left = sums.query(mid_pos)

            left_cost = median * count_left - sum_left
            right_cost = (total - sum_left) - median * (x - count_left)

            return left_cost + right_cost

        costs.append(get_cost())

        # Sliding window
        for i in range(x, n):
            old = nums[i - x]
            new = nums[i]

            freq.add(pos[old], -1)
            sums.add(pos[old], -old)

            freq.add(pos[new], 1)
            sums.add(pos[new], new)

            total += new - old

            costs.append(get_cost())

        # Dynamic Programming
        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):

                # Skip current element
                dp[i][j] = dp[i - 1][j]

                # Select window of size x
                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x]
                    )

        return dp[n][k]
