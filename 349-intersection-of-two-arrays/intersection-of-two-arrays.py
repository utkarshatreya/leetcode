class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s = set(nums1)
        result = []

        for num in nums2:
            if num in s:
                result.append(num)
                s.remove(num)
        return result        