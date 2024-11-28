class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        sum = 0
        for num in nums:
            sum+=num
            prefix_sum.append(sum)
        
        max = prefix_sum[-1]
        for i in range(1, len(prefix_sum)):
            if prefix_sum[i-1] == max-prefix_sum[i]:
                return i-1
        return -1
        

        




            

        # brute force
        # for i in range(len(nums)):
        #     left_array = nums[:i]
        #     right_array = nums[i+1:]
        #     left_sum = 0
        #     right_sum = 0
        #     for left in left_array:
        #         left_sum += left
        #     for right in right_array:
        #         right_sum += right
        #     if left_sum == right_sum:
        #         return i
        # return -1
        

        