class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    
        ans = 0 
        for i in range(len(s)-1):
            cur_char = s[i]
            next_char = s[i+1]
            cur_val = roman_map[cur_char]
            next_val = roman_map[next_char]
            if cur_val < next_val:
                ans -= cur_val
            else:
                ans += cur_val
        ans += roman_map[s[-1]]
        return ans 