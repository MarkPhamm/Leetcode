class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        curr = []

        def backtrack(start):
            if curr not in ans:
                ans.append(curr[:])

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()
            
        backtrack(0)
        return ans