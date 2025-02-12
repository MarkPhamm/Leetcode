class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # brute force:
        while part in s:
            s = s.replace(part, "", 1)
        
        return s
        