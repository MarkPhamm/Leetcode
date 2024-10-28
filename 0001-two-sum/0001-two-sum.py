class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return dict[complement], index
            else: 
                dict[num] = index
