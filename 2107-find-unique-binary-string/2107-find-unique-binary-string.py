class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        perm = []
        curr = []

        def backtrack(curr):
            if len(curr) == len(nums[0]):
                perm.append("".join(curr[:]))
                return
            
            for i in range(2):
                curr.append(str(i))
                backtrack(curr)
                curr.pop()
        
        backtrack(curr)
        for p in perm:
            if p not in nums:
                return p
        