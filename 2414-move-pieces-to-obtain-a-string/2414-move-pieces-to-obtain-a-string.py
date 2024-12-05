class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_","") != target.replace("_",""):
            return False
        
        i = 0
        j = 0

        while i < len(start) and j < len(target):
            if start[i] == "_":
                i+=1
            elif start[i] == "L":
                if target[j] != 'L':
                    j+=1
                else:
                    if i<j:
                        return False
                    else:
                        i+=1
                        j+=1
            elif start[i] == "R":
                if target[j] != "R":
                    j+=1
                else:
                    if i>j:
                        return False
                    else:
                        i+=1
                        j+=1
        return True

        