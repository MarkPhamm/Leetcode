class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)

        l, r = 0, len(nums) - 1
        ans = -1
        while l < r:
            current_sum = nums[l] + nums[r]
            if nums[l] + nums[r] < k:
                ans = max(ans, current_sum)
                l = l + 1
            else:
                r = r -1
        return ans