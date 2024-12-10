class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for char in s:
            counter[char] = counter.get(char,0)+1
        
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1