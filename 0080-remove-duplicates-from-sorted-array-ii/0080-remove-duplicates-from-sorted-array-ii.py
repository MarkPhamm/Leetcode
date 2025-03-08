class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1  # Position where the next valid element should be placed
        count = 1  # Counts occurrences of the current number

        for i in range(1, len(nums)):  # Start from index 1
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1  # Reset count for a new number
            
            if count <= 2:  # Allow at most two duplicates
                nums[k] = nums[i]
                k += 1
        
        return k
        