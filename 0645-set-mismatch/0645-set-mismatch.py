class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        set_nums = set(nums)
        set_all = set(i for i in range(1,len(nums)+1))
        difference = list(set_all.difference(set_nums))[0]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return [nums[i], difference]
        

        
        