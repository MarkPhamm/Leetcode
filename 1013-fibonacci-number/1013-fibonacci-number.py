class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        memo = [0,0,1]
        for i in range (2,n+1):
            memo[0] = memo[1]
            memo[1] = memo[2]
            memo[2] = memo[1] + memo[0]
        return memo[2]