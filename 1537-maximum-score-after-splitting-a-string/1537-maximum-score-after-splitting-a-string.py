class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            left_str = s[:i]
            right_str = s[i:]
            score = left_str.count("0") + right_str.count("1")
            max_score = max(score, max_score)
        
        return max_score
        