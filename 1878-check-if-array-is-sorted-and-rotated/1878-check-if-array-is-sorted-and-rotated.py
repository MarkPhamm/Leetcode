class Solution:
    def check(self, nums: List[int]) -> bool:
        # rotating nums in every possible way
        sort_nums = sorted(nums)
        rotated_nums = nums
        for i in range(len(rotated_nums)):
            rotated_nums = [rotated_nums[-1]] + rotated_nums[:-1]
            if rotated_nums == sort_nums:
                return True

        return False
        