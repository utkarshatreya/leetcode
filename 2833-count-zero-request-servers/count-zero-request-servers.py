class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        q = sorted((t, i) for i, t in enumerate(queries))

        count = [0] * (n + 1)
        ans = [0] * len(queries)

        left = right = 0
        active = 0
        m = len(logs)

        for t, idx in q:
            start = t - x

            # Add logs inside the right boundary
            while right < m and logs[right][1] <= t:
                server = logs[right][0]

                if count[server] == 0:
                    active += 1

                count[server] += 1
                right += 1

            # Remove logs outside the left boundary
            while left < right and logs[left][1] < start:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans