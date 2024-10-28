class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to_remove = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                to_remove.append(i)
        
        for index, remove in enumerate(to_remove):
            nums.pop(remove-index)
   