class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                s = s.replace(i, "", 1)
                t = t.replace(i, "", 1)
        return len(s) == 0 and len(t) == 0
        