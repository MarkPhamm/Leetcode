class Solution:
    # Base case: n <= 2: F(n) = n ways to climb the stairs
    # if n > 2: there are F(n) = F(n-1) + F(n-2)
    # @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2 
        for i in range(3, n+1):
            ans = dp[i-1] + dp[i-2]
            dp[i] = ans 
        return dp[-1]