class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        lookup = {}
        total = sum(nums)
        outlier = -1

        # saving index
        for index, val in enumerate(nums):
            lookup[val] = index

        res = float('-inf')

        for i, num in enumerate(nums):
            curr_sum = total-num
            if curr_sum%2 == 0:
                val = curr_sum/2
                if val in lookup and lookup[val] != i:
                    res = max(res, num)
        
        return res

