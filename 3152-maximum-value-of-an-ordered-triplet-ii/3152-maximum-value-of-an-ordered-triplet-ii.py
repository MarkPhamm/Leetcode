class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_cur = nums[0]
        max_diff = -math.inf
        ans = 0

        for i in range(1, len(nums)-1):
            prev = nums[i-1]
            next = nums[i+1]

            max_cur = max(prev, max_cur)
            max_diff = max(max_cur - nums[i], max_diff)
            ans = max(max_diff * next, ans)
        return ans


        