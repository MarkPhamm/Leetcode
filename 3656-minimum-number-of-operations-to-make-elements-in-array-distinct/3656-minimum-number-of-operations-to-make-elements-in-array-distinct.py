class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        while len(nums) != len(set(nums)):
            if len(nums) >= 3:
                nums = nums[3:]
            else:
                nums = []
            ans +=1
        return ans