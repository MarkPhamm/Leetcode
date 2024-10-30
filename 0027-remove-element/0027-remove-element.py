class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1 
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j-=1
            else:
                i+=1
        return j+1


# Time complexity(O(n^2))
# Space complexity((O(1)))
        
# [0,1,2,2,3,0,4,2] -> [0,1,2,3,0,4,2,"_"] -> [0,1,3,0,4,2,"_","_"] -> [0,1,3,0,4,"_","_","_"]

