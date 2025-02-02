class Solution:
    def checkString(self, s: str) -> bool:
        last_a = -inf
        first_b = +inf
        for i in range(len(s)):
            if s[i] == "a":
                last_a = max(i, last_a)
            else:
                first_b = min(i, first_b)
        
        return last_a < first_b
        