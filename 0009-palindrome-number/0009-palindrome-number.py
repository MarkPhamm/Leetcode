class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        l = 0 
        r = len(string_x) - 1

        while l < r: 
            if string_x[l] == string_x[r]:
                l+=1 
                r-=1
            else:
                return False 
        
        return True 
        