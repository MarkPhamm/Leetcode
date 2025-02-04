class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        n = len(nums)
        cur_sum = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cur_sum +=  nums[i]
                ans = max(ans, cur_sum)
            else:
                cur_sum = nums[i]
                ans = max(ans, cur_sum)
        
        return ans
        