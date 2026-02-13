class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False

        lookup = {}
        for char in s:
            lookup[char] = lookup.get(char, 0) + 1
        
        for char in t:
            lookup[char] = lookup.get(char, 0) - 1
            if lookup[char] == 0:
                del(lookup[char])
        
        return len(lookup) == 0

        