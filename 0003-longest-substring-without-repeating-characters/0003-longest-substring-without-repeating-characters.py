class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        ans = 0

        for r, c in enumerate(s):
            while c in seen:
                if s[l] in seen:
                    seen.remove(s[l])
                l+=1
            seen.add(c)
            ans = max(ans, r - l + 1)
        return ans    
