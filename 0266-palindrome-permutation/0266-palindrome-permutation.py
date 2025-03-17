from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashmap = Counter(s)
        odd = 0
        for val in hashmap.values():
            if val % 2 == 1:
                odd +=1 
        return odd <= 1
        
        