from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_dict = Counter(words1)
        words2_dict = Counter(words2)
        
        ans = 0
        for w in words1:
            if words1_dict[w] == 1:
                if w in words2_dict and words2_dict[w] == 1:
                    ans +=1
        return ans
        
