class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # n = len(nums)
        # exchanges = 0
        # i = 0
        # while i < n:
        #     if nums[i] == val:
        #         nums.pop(i)
        #         nums.append("_")
        #         exchanges += 1
        #         i-=1
        #     i+=1
        # print(nums)
        # return n-exchanges
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n-=1
            else:
                i+=1
        return n




        
        