class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        i=0
        j=i+1
        while i<j and j<len(s) :
            diff=abs(ord(s[i])-ord(s[j]))
            sum+=diff
            i+=1
            j+=1
        return sum
        