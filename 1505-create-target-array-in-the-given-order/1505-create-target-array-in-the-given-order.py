class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        results = []
        for i in range(len(nums)):
            if len(results) == index[i]:
                results.append(nums[i])
            else:
                results = results[:index[i]] + [nums[i]] + results[index[i]:]
        return results     