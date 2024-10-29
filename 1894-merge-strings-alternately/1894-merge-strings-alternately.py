class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # result = ""
        # common_length = len(word1) if len(word1) < len(word2) else len(word2)
        # for i in range(common_length):
        #     result += word1[i]
        #     result += word2[i]
        # result += word1[common_length:]
        # result += word2[common_length:]
        # return result

        results = ""
        common_length = min(len(word1), len(word2))
        for i in range(common_length):
            results += word1[i]
            results += word2[i]
        if len(word1) > common_length:
            results += word1[common_length:]
        if len(word2) > common_length:
            results += word2[common_length:]
        return results



    
        
        