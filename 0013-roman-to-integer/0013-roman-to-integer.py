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
        n = len(s)
        i = 0
        while i < n:
            if i == n-1:
                sum+=dict[s[i]]
                i+=1
            elif dict[s[i]] >= dict[s[i+1]]:
                total = dict[s[i]]
                sum+=total
                i+=1
            else:
                total = -dict[s[i]] + dict[s[i+1]]
                sum+=total
                i+=2
        return sum
        