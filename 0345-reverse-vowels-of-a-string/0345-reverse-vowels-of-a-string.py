class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u"]
        s_list = list(s)

        l = 0 
        r = len(s)-1
        if len(s) == 1:
            return s

        while l < r:
            if s_list[l].lower() in vowels and s_list[r].lower() not in vowels:
                r-=1
            elif s_list[l].lower() not in vowels and s_list[r].lower() in vowels:
                l+=1
            elif s_list[l].lower() in vowels and s_list[r].lower() in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l+=1
                r-=1
            else: 
                l+=1
                r-=1
        return "".join(s_list)
        