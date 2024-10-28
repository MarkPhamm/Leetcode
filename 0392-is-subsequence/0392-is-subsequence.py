class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        j = 0         
        n = len(t)
        while i <= len(t)-1 and j<= len(s)-1:
            if t[i] == s[j]:
                j+=1
            i+=1
        return(j == len(s))