
class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        mini = min(nums)
        maxi = max(nums)

        if mini == maxi:
            return 0

        # Calculate bucket size
        bucket_size = max(1, (maxi - mini + n - 2) // (n - 1))

        # Calculate number of buckets
        bucket_count = (maxi - mini) // bucket_size + 1

        # Each bucket stores [minimum, maximum]
        buckets = [[float('inf'), float('-inf')]
                   for _ in range(bucket_count)]

        # Put numbers into buckets
        for num in nums:
            index = (num - mini) // bucket_size

            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

        max_gap = 0
        prev_max = mini

        # Check gaps between buckets
        for b_min, b_max in buckets:
            if b_min == float('inf'):
                continue

            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max

        return max_gap
