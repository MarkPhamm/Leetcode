class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        ans = 0

        for char in s:
            if char == "(":
                stack.append("(")
                depth +=1
                ans = max(ans, depth)
            elif char == ")":
                stack.pop()
                depth -=1
        
        return ans

        