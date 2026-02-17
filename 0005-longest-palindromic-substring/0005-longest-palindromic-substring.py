class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ans_length = 0
        
        n = len(s) 

        for i in range(n):
            l = i
            r = i

            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > ans_length:
                    ans = s[l:r+1]
                    ans_length = r - l + 1
                l-=1
                r+=1

            l = i
            r = i+1

            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > ans_length:
                    ans = s[l:r+1]
                    ans_length = r - l + 1
                l-=1
                r+=1
        return ans 
