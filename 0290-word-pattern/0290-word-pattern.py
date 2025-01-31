class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        hashmap_reverse = {}
        if len(pattern) != s.count(" ")+1:
            return False

        s = split(' ', s)


        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                hashmap[pattern[i]] = s[i]
            else:
                if hashmap[pattern[i]] != s[i]:
                    return False
        
        for i in range(len(pattern)):
            if s[i] not in hashmap_reverse:
                hashmap_reverse[s[i]] = pattern[i]
            else:
                if hashmap_reverse[s[i]] != pattern[i]:
                    return False
        
        return True
            
        