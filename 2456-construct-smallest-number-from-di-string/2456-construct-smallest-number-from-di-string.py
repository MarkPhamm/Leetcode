class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Idea
        # Step 1: initiate n: len(pattern), stack: arr, and ans: str
        # Step 2:
        # 2.1: loop through the index of pattern: add the index to the stack
        # 2.2 if the pattern[index] = "I" or pattern already at the end, insert all the value of the stack to Answer
        # Step 3: return ans
        n = len(pattern)
        ans = ""
        stack = []

        for i in range(n+1):
            stack.append(i+1)
            if i == n or pattern[i] == 'I':
                while stack:
                    ans+=str(stack[-1])
                    stack.pop()

        return ans
