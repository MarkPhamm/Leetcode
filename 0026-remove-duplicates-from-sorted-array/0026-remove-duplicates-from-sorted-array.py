class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Solution 1: to delete method
        # to_delete = []
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         to_delete.append(i)
        
        # for index, delete in enumerate(to_delete):
        #     nums.pop(delete-index)
        
        # return len(nums)

        # Solution 2: two pointer: fast flow pointer Time O(n) , Space O(1)
        s = 1 
        for f in range(1, len(nums)): 
            if nums[f] != nums[f-1]: # check if fast pointer diff fast at index -1 
               nums[s] = nums[f]
               s+=1
            else:
                pass # else just increase the fast pointer
        return s
