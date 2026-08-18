class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Case 1: k == 1
        if k == 1:
            count = Counter(nums)

            ans = -1
            for num in nums:
                if count[num] == 1:
                    ans = max(ans, num)

            return ans

        # Case 2: k == n
        if k == n:
            return max(nums)

        # Case 3: 1 < k < n
        count = Counter(nums)

        ans = -1

        if count[nums[0]] == 1:
            ans = max(ans, nums[0])

        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans