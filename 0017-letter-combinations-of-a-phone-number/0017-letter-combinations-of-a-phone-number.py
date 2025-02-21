class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        ans = []
        current_solution = []

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


        def chose(i):
            # chose letter i for the array of char

            # Base case: stop when you are in the last character
            if i == len(digits):
                ans.append("".join(current_solution))
                return
            
            # recursive
            for next_char in digit_mapping[digits[i]]:
                # current sol = ["a"], next number = 3
                # --> ["a" , "d"], ["a" , "e"], ["a" , "f"]
                current_solution.append(next_char)

                # check the next charter 
                chose(i+1)
        
                current_solution.pop()
        
        chose(0)
        return ans    
        