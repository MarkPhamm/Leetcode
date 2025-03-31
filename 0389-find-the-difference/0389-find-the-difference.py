from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap_s = Counter(s)
        hashmap_t = Counter(t)

        for k in hashmap_t.keys():
            if k not in hashmap_s.keys() or hashmap_t[k] != hashmap_s[k]:
                return k
        
        