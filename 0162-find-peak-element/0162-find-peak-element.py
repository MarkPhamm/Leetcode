from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:  # Move towards the increasing slope
                l = mid + 1
            else:  # nums[mid] > nums[mid + 1], move left (possible peak)
                r = mid

        return l  # l == r, which is a peak index
