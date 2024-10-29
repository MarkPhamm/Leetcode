class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        val = min(abs(x) for x in nums)
        if val in nums:
            return val
        return -val

        