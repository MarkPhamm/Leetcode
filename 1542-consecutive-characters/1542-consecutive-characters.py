class Solution:
    def maxPower(self, s: str) -> int:
        # Two Pointer
        # i = 0
        # j = 0
        # longest = 0

        # s = s+"0"

        # while i < len(s):
        #     if s[i] != s[j]:
        #         longest = max(longest, i-j)
        #         j = i
        #     i+=1
        
        # return longest
        
        current_sum = 0
        max_sum = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current_sum +=1
                max_sum = max(current_sum, max_sum)
            else:
                current_sum = 0
        
        return max_sum+1



        