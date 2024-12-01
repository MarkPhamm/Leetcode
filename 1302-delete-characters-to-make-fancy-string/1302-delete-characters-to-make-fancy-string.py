class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        threshold = len(s)-3
        while i <= threshold:
            if s[i] == s[i+1] and s[i] == s[i+2]:
                s = s[:i]+s[i+1:]
                threshold -=1
            else:
                i+=1
        return s


        