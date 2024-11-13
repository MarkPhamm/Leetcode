class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count+=1
                max_count = max(current_count, max_count)
            else:
                current_count = 0

        return max_count
        
        # longest_streak = 0
        # nums = nums + [0]
        # i = 0
        # j = 0
        # while i <= len(nums)-1:
        #     if nums[i] == 0 and nums[j] == 1:
        #         longest_streak = max(longest_streak, i-j)
        #         j = i
        #     elif nums[i] == 1 and nums[j] == 0:
        #         j = i
        #     else:
        #         i+=1
        # return longest_streak
    
        
        