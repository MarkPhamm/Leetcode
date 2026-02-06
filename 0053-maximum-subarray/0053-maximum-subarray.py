class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        ans = nums[0]

        for n in nums:
            if cur < 0:
                cur = 0
            cur = n + cur
            ans = max(ans, cur)
        
        return ans 