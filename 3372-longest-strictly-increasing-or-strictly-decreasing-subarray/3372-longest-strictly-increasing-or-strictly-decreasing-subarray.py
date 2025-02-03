class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_asc = max_desc = 1
        current_asc = current_desc = 1
        
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                current_asc += 1
                max_asc = max(max_asc, current_asc)
                current_desc = 1
            elif nums[i+1] < nums[i]:
                current_desc += 1
                max_desc = max(max_desc, current_desc)
                current_asc = 1
            else:
                current_asc = current_desc = 1
        
        return max(max_asc, max_desc)
