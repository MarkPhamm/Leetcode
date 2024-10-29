class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
    
        sum = 0
        i = 0
        n = len(s)
        while i < n:
            if i < n-1 and dict[s[i]] < dict[s[i+1]]:
                sum+= dict[s[i+1]] - dict[s[i]]
                i+=2
            else:
                sum+= dict[s[i]]
                i+=1
        return sum
