class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        prev = lower - 1  # Start from one before the lower bound
        
        # Append a virtual `upper + 1` to cover the last missing range
        nums.append(upper + 1) 
        
        for num in nums:
            if num > prev + 1:
                ans.append([prev + 1, num - 1])
            prev = num  # Move `prev` forward
        
        return ans