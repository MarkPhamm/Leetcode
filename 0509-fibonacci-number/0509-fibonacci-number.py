@lru_cache(None)
class Solution():
    # Step 1: Define F
    # Step 2: Base case: F(0) = 0, F(1) = 1
    # Step 3: Recursive relation: F(n) = F(n-1) + F(n-2) 
    # Step 4: Implementation

    # TC: O(n)
    # SC: O(n)
    
    def fib(self, n):
        def recursion_sol(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return self.fib(n-1) + self.fib(n-2)   
        
        def dp_sol(n):
            dp = [0] * (n+1)
            if n <= 1:
                return n
            dp[1] = 1
            for i in range(2,n+1):
                next = dp[i-1] + dp[i-2]
                dp[i] = next
            print(dp)
            return dp[-1]
        
        return dp_sol(n)