class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 0:
            return 0
        while n > 0:
            remainder = n%3
            if remainder == 2:
                return False
            n//=3
        return True
        