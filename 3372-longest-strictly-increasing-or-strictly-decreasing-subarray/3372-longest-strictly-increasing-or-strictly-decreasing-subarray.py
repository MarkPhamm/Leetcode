class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_asc = max_desc = 1
        current_asc = current_desc = 1
        
        for i in range(n-1):
            # if the next number is larger than the current number
            if nums[i+1] > nums[i]:
                # increase current_ascending
                current_asc += 1
                # update max_asc
                max_asc = max(max_asc, current_asc)
                # reset current_descending
                current_desc = 1
            # if the next number is smaller than the current number
            elif nums[i+1] < nums[i]:
                # increase current_descending
                current_desc += 1
                # update max_desc
                max_desc = max(max_desc, current_desc)
                # reset current_ascending
                current_asc = 1
            else:
                # reset both current_asc and current_desc
                current_asc = current_desc = 1
        
        return max(max_asc, max_desc)
