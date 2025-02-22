class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        ans = []
        curr = []

        digit_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }


        def backtrack(index):
            if len(curr) == len(digits):
                ans.append("".join(curr.copy()))
                return 
            
            for char in digit_mapping[digits[index]]:
                curr.append(char)
                backtrack(index+1)
                curr.pop()
            
        backtrack(0)
        return ans