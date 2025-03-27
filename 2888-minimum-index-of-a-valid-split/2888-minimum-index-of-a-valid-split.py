from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        dominant = max(count, key=count.get)
        total_count = count[dominant]


        left_count = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                left_count += 1
                right_count = total_count - left_count
            
            left_threshold = (i+1)/2
            right_threshold = (len(nums) - (i + 1))/2

            if left_count > left_threshold and right_count > right_threshold:
                return i
        return -1

            
                