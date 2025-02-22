class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        nums.sort()

        def backtrack(curr):
            ans.append(curr[:])

            for num in nums:
                if num not in curr:
                    if curr and curr[-1] < num:
                        return
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        
        backtrack(curr)
        return ans
