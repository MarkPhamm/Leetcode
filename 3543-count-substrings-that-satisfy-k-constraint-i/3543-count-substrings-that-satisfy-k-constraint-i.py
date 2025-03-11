class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        nums_zero = 0
        nums_one = 0
        l = 0
        ans = 0
        for r, char in enumerate(s):
            if char == "1":
                nums_one +=1
            if char == "0":
                nums_zero +=1
            while nums_zero > k and nums_one > k:
                if s[l] == "1":
                    nums_one -=1
                if s[l] == "0":
                    nums_zero -=1
                l+=1
            ans += (r - l + 1)
        return ans
            
                
        