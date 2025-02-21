class Solution:
    # Base case: n <= 2: F(n) = n ways to climb the stairs
    # if n > 2: there are F(n) = F(n-1) + F(n-2)
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        