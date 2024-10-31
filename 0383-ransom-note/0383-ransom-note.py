class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter = 0
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char, "", 1)
            else: 
                letter +=1
        
        return letter == 0
        