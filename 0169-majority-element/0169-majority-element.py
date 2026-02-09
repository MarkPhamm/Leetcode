class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0 

        for n in nums:
            if n == res:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 1
                    res = n 
        return res 