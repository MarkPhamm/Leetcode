class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        exchanges = 0
        i = 0
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                nums.append("_")
                exchanges += 1
                i-=1
            i+=1
        print(nums)
        return n-exchanges
        
        