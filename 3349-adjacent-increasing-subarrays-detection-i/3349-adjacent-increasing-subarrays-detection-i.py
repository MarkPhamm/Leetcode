class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # [2,5,7,8,9,2,3,4,3,1]       
        total_length = 2*k
        n = len(nums)

        if k == 1:
            return n>=2

        for i in range(0, n - total_length + 1):
            sub_array = nums[i:i+total_length] 
            left_sub = sub_array[:k]
            right_sub = sub_array[k:]

            valid = True  
            for i in range(1,k):
                if left_sub[i] <= left_sub[i-1] or right_sub[i] <= right_sub[i-1]:
                    break
            else: 
                return True
        return False 