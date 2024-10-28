class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        common_len = (len(word1) if len(word1) < len(word2) else len(word2))
        alternate_string = ""
        for i in range(common_len):
            alternate_string += word1[i]
            alternate_string += word2[i]
        
        alternate_string += word1[common_len:]
        alternate_string += word2[common_len:]
        return alternate_string
        
        