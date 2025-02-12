class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)
        
        for char in s:
            stack.append(char)
            # Check if the end of the stack matches 'part'
            if len(stack) >= part_length and "".join(stack[-part_length:]) == part:
                del stack[-part_length:]  # Remove the matched part
                
        return "".join(stack)