class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = ""
        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or strs[0][i] != str[i]:
                    return result
            result += strs[0][i]
        return result
            