class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        CounterBadLet = 0
    
        for char in ransomNote:
            if char not in magazine:
                CounterBadLet += 1
            else:
                magazine = magazine.replace(char, "", 1)

        return CounterBadLet == 0
        
        