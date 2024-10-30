class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        magazine_dict = {}

        for i in ransomNote:
            if i not in ransomNote_dict:
                ransomNote_dict[i] = 1
            else: 
                ransomNote_dict[i] += 1
        print(ransomNote_dict)

        for j in magazine:
            if j not in magazine_dict:
                magazine_dict[j] = 1
            else: 
                magazine_dict[j] += 1
        print(magazine_dict)
        
        for z in ransomNote_dict:
            if z not in magazine_dict:
                return False
            elif ransomNote_dict[z] > magazine_dict[z]:
                return False
        return True
            
        
        