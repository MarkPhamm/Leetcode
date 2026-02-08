# TLDR: # store the compensate and current index 
# Eg: nums = [2,7,11,15] seen = {7:0}
# if found current pair: reuturn 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for k,v in enumerate(nums):
            # print(seen)
            if v not in seen:
                seen[target-v] = k # store the compensate and current index
            else: 
                return [seen[v], k] # if we found the pair
        