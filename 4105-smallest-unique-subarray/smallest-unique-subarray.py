class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        mod1 = 10**9 + 7
        mod2 = 10**9 + 9

        base1 = 911382323
        base2 = 972663749

        def check(length):
            pow1 = pow(base1, length - 1, mod1)
            pow2 = pow(base2, length - 1, mod2)

            h1 = 0
            h2 = 0

            # Calculate first window hash
            for i in range(length):
                h1 = (h1 * base1 + nums[i]) % mod1
                h2 = (h2 * base2 + nums[i]) % mod2

            freq = {}

            key = (h1, h2)
            freq[key] = 1

            
            for i in range(length, n):
                h1 = ((h1 - nums[i - length] * pow1) * base1
                      + nums[i]) % mod1

                h2 = ((h2 - nums[i - length] * pow2) * base2
                      + nums[i]) % mod2

                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            return 1 in freq.values()

        # Binary Search
        left, right = 1, n
        ans = n

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
