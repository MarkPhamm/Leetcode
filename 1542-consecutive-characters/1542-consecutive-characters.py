class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        j = 0
        longest = 0

        s = s+"0"

        while i < len(s):
            if s[i] != s[j]:
                longest = max(longest, i-j)
                j = i
            i+=1
        
        return longest


        