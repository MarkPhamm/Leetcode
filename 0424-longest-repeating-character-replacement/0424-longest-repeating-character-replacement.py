class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0

        l = 0

        for r in range(len(s)):
            length = r - l + 1
            count[s[r]] = count.get(s[r], 0) + 1
            if length - max(count.values()) > k: # invalid
                count[s[l]] -=1
                l+=1
            ans = max(r-l+1, ans)
        return ans  

            