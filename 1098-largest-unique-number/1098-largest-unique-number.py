class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0)+1
        
        ans = -1
        for key, val in counter.items():
            if val == 1:
                ans = max(ans, key)
        
        return ans