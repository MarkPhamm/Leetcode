class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def brute_force(self, nums: List[int], target: int) -> List[int]:
            ans = []
            nums.sort()
            for i in range(len(nums)):
                if nums[i] == target:
                    ans.append(i)
            return ans
        
        return brute_force(self, nums, target)