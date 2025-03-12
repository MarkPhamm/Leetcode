class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashmap = defaultdict(int)
        ans = 0
        l = 0

        for r, char in enumerate(s):
            hashmap[char] += 1
            
            # slide left when there's all 3 characters
            while len(hashmap) == 3:
                hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0:
                    del(hashmap[s[l]])
                l += 1
            
            ans += l
            
        return ans
        