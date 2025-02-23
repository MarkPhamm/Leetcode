class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_set = set(nums)
        n = len(nums[0])

        def backtrack(curr):
            if len(curr) == len(nums[0]):
                candidate = "".join(curr[:])
                if candidate not in num_set:
                    return candidate
                return
            
            for i in "01":
                curr.append(i)
                candidate = backtrack(curr)
                if candidate:
                    return candidate
                curr.pop()
        
        return backtrack([])
        