class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        cur_sum = 0
        prefix = []
        for num in nums:
            cur_sum = cur_sum + num
            prefix.append(cur_sum)
        print(prefix)
       
        ans = 0
        for i in range(0,len(nums)-1):
            if prefix[i] >= prefix[len(prefix)-1] - prefix[i]:
                ans +=1
        return ans

