class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        current = 0
        ans = 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                current+=1
                ans = max(current,ans)
            elif nums[i+1] == nums[i]:
                continue
            else:
                current = 0
        
        return ans+1
            
        