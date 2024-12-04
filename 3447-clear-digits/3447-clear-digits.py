class Solution:
    def clearDigits(self, s: str) -> str:
        alpha_stack = []
        for char in s:
            if char.isalpha():
                alpha_stack.append(char)
            elif char.isdigit():
                alpha_stack.pop()
        return "".join(alpha_stack)