class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char.isupper():
                if stack and char.lower() == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                if stack and char.upper() == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
        
        return "".join(stack)