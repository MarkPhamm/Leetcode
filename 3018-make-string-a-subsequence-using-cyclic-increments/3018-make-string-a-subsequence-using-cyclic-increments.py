class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        lookup = {chr(i): chr(i + 1) for i in range(97, 122)}
        lookup['z'] = 'a'
        
        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or lookup[str1[i]] == str2[j]:
                j+=1
                i+=1
            else:
                i+=1
        
        print(j)
        if j == len(str2):
            return True
        return False
    
        
        