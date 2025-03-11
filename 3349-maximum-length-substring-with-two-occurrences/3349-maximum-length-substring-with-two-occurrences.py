class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hashmap = defaultdict(int) 
        print(hashmap)
        
        l = 0
        ans = 0

        for r, char in enumerate(s):
            hashmap[char] +=1
            while hashmap[char] > 2:
                hashmap[s[l]] -=1
                l+=1
            ans = max(ans, r-l+1)
        return ans                    