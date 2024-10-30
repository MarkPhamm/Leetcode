class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        occurence = 0
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                nums.append("_")
                i-=1
                occurence +=1
            i+=1
        print(occurence)
        return n-occurence

# Time complexity(O(n^2))
# Space complexity((O(1)))
        
# [0,1,2,2,3,0,4,2] -> [0,1,2,3,0,4,2,"_"] -> [0,1,3,0,4,2,"_","_"] -> [0,1,3,0,4,"_","_","_"]