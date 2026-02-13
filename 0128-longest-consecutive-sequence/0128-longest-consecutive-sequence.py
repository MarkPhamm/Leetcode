class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        ans = 0

        for n in set_nums:
            if n-1 not in set_nums: # This is the start of the sequence
                length = 0 
                while (n+length) in set_nums:
                    length+=1
                    ans = max(length, ans)
        return ans 