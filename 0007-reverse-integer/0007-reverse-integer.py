class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if x == 0:
            return 0
        elif x > 0:
            rev = int(str(x)[::-1])
        else:
            rev = -int(str(abs(x))[::-1])

        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev