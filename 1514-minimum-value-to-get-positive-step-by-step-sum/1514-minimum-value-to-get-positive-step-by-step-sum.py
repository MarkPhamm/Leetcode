class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]*(n)
        prefix_sum[0] = nums[0]
        min = nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            if prefix_sum[i]<min:
                min = prefix_sum[i]
        print(prefix_sum)

        return -min+1 if min < 0 else 1
        
        
        