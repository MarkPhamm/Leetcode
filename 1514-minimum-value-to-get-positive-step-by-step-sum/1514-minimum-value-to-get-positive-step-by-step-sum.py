class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix = float('inf')

        for num in nums:
            prefix_sum += num
            min_prefix = min(min_prefix, prefix_sum)
        
        return -min_prefix + 1 if min_prefix < 0 else 1
