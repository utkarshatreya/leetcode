
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)

        total = 0

        for num in nums:
            total += maximum - num

        return total
