class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        cur_sum = 0
        ans = math.inf
        for r, num in enumerate(nums): # (index, value)
            cur_sum  += num
            while cur_sum >= target:
                ans = min(ans, r - l + 1)
                cur_sum -= nums[l]
                l +=1
        return 0 if ans == math.inf else ans