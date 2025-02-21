class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(start, curr):
            ans.append(curr[:])
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return ans