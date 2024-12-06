class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        banned_set = set(banned)
        cur_sum = 0
        
        for i in range(1,n+1):
            if i not in banned_set and cur_sum+i <= maxSum:
                cur_sum+=i
                count+=1
        return count

