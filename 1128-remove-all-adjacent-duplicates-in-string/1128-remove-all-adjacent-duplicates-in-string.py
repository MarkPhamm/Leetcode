class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = [0]
        for char in s:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack[1:])
        