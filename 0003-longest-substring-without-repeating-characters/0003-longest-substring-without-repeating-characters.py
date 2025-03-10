class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashmap = {}
        ans = 0 
        for r, char in enumerate(s): # (index, value)
            # update left to the last seen index + 1
            if char in hashmap and hashmap[char] >= l:
                l = hashmap[char] + 1

            # adding index to the hashmap of r
            hashmap[char] = r
            ans = max(ans, r - l + 1)
        return ans    