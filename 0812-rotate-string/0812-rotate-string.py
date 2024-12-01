class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        double = goal+goal
        if s in double:
            return True
        return False
        
        