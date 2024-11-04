class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        nc = set(s)
        for i in nc:
            if s.count(i) != t.count(i):
                return False
        return True