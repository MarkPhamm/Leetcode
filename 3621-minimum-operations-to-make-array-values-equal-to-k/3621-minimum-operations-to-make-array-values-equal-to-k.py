class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        if min(nums) < k: 
            return -1

        max_val = max(nums)
        count = 0
        nums = set(nums)

        for num in nums:
            if num == max_val:
                continue
            
            if num >= k:
                count += 1
        
        return count if k == min(nums) else count + 1

