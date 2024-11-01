class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                i = i-j+1
                j=0
        return i-j