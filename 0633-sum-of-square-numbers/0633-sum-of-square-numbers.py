class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = ceil(sqrt(c))
        while l <= r:
            square = r**2 + l**2
            mid = ceil((l+r)/2)
            if square == c:
                return True
            elif square > c:
                r -=1
            elif square < c:
                l +=1
        return False
        