#Loop through each element x and find if there is another value that equals to (target - x)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for k,v in enumerate(nums):
            if v not in seen:
                seen[target-v] = k # store the compensate and current index
            else: 
                return [seen[v], k] # if we found the pair
        print(seen)
        