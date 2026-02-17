class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        first_str = strs[0]

        for i in range(len(first_str)):
            check_char = first_str[i]
            for remaining_str in strs[1:]:
                if  i == len(remaining_str) or check_char != remaining_str[i]:
                    return ans 
            ans += check_char
        
        return ans