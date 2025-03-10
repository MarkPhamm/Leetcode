from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        l = 0
        cnt = Counter(p)
        ans = []

        for r, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s[l]] +=1
                l+=1
            if r - l + 1 == len(p):
                ans.append(l)
        return ans
        

        