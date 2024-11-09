class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a','i','e','o','u']
        for i in s:
            if i in vowels:
                s = s.replace(i, "")
        
        return s
        