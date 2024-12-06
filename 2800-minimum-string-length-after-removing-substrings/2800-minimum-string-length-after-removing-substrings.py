class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if "AB" in s or "CD" in s:
                s = s.replace("AB","",1)
                s = s.replace("CD","",1)
            else:
                break
        
        return len(s)